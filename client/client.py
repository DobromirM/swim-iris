import asyncio
import websockets
import re

from utils.record import Record


def create_downlink_message(node, lane, value=None):
    return f'@sync(node:"{node}",lane:{lane})'


def create_record(response):
    response = re.findall(r"\{(.*)\}", response)

    if len(response) > 0:
        message = response[0]

        record = Record()
        record.create_from_string(message)
        return record


async def run():
    uri = "ws://localhost:9001"
    async with websockets.connect(uri) as websocket:
        message = create_downlink_message('/training/1', 'data')
        await websocket.send(message)

        while True:
            response = await websocket.recv()

            if 'Record' in response:
                record = create_record(response)
                print(record)
            else:
                print(response)


asyncio.get_event_loop().run_until_complete(run())
