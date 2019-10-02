import asyncio
import websockets
import re

from globals import TRAINING_DATA, ML, GROUND_TRUTH_DATA
from ml.record import Record, RecordType
from ml.utils import IrisLabels

NUMBER_OF_SAMPLES_FOR_RETRAIN = 5


def create_downlink_message(node, lane):
    return f'@sync(node:"{node}",lane:{lane})'


def create_record(response):
    response = re.findall(r"\{(.*)\}", response)

    if len(response) > 0:
        message = response[0]

        record = Record()
        record.create_from_string(message)
        return record


def handle_training_record(record):
    TRAINING_DATA.add_data(record.as_data_frame())

    if TRAINING_DATA.size % NUMBER_OF_SAMPLES_FOR_RETRAIN == 0:
        ML.fit(TRAINING_DATA.data)
        accuracy = ML.measure_accuracy(GROUND_TRUTH_DATA.data)
        print(f'The accuracy of KNN is:{accuracy}')


def handle_testing_record(record):
    try:
        prediction = ML.predict(record.as_data_frame())

        if len(prediction) == 1:
            prediction = prediction[0]

            truth = GROUND_TRUTH_DATA.data.loc[record.index]['label'].astype(int)

            print(f'Prediction for record {record.index} is: {IrisLabels.get_name(prediction)} (Truth: {IrisLabels.get_name(truth)})')

    except Exception:
        print('The model cannot predict yet, because it has not been trained.')


async def open_downlink(uri, node, lane):
    async with websockets.connect(uri) as websocket:
        message = create_downlink_message(node, lane)
        await websocket.send(message)

        while True:
            response = await websocket.recv()

            if 'Record' in response:
                record = create_record(response)

                print(record)

                if record.type == RecordType.TESTING:
                    handle_testing_record(record)
                else:
                    handle_training_record(record)

            else:
                print(response)


async def run(uri, agents):
    await asyncio.wait([open_downlink(uri, node, lane) for node, lane in agents])
