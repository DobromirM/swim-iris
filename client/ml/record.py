import pandas as pd
from globals import TRAINING_DATA, ML, GROUND_TRUTH_DATA
from ml.utils import IrisLabels

NUMBER_OF_SAMPLES_FOR_RETRAIN = 5


def handle_training_record(record):
    TRAINING_DATA.add_data(record.as_data_frame())

    if TRAINING_DATA.size % NUMBER_OF_SAMPLES_FOR_RETRAIN == 0:
        ML.fit(TRAINING_DATA.data)
        accuracy = ML.measure_accuracy(GROUND_TRUTH_DATA.data)

        with open('output/accuracies.txt', 'a') as output_file:
            output_file.write(f'{accuracy}\n')

        print(f'The accuracy of KNN is:{accuracy}')


def handle_testing_record(record):
    try:
        prediction = ML.predict(record.as_data_frame())

        if len(prediction) == 1:
            prediction = prediction[0]

            truth = GROUND_TRUTH_DATA.data.loc[record.index]['label'].astype(int)

            with open('output/testing_results.txt', 'a') as output_file:
                output_file.write(f'{1 if prediction == truth else 0}\n')

            print(
                f'Prediction for record {record.index} is: {IrisLabels.get_name(prediction)} (Truth: {IrisLabels.get_name(truth)})')

    except Exception:
        print('The model cannot predict yet, because it has not been trained.')


class TrainingRecord:

    def __init__(self, index=0, sepal_length=0, sepal_width=0, petal_length=0, petal_width=0,
                 label=0):
        self.index = int(index)
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)
        self.label = int(label)

    def as_data_frame(self):
        dict_rep = {'sepal_length': self.sepal_length, 'sepal_width': self.sepal_width,
                    'petal_length': self.petal_length,
                    'petal_width': self.petal_width, 'label': self.label}

        return pd.DataFrame(dict_rep, index=[self.index])

    def __str__(self):
        return f'TrainingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width},' \
               f' petal_length={self.petal_length}, petal_width={self.petal_width}, label={self.label})'


class TestingRecord:
    def __init__(self, index=0, sepal_length=0, sepal_width=0, petal_length=0, petal_width=0):
        self.index = int(index)
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)

    def as_data_frame(self):
        dict_rep = {'sepal_length': self.sepal_length, 'sepal_width': self.sepal_width,
                    'petal_length': self.petal_length,
                    'petal_width': self.petal_width}

        return pd.DataFrame(dict_rep, index=[self.index])

    def __str__(self):
        return f'TestingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width},' \
               f' petal_length={self.petal_length}, petal_width={self.petal_width})'
