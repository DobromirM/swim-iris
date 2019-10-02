import pandas as pd

from ml.utils import convert_camel_to_snake
from enum import Enum


class RecordType(Enum):
    TRAINING = 0
    TESTING = 1


class Record:

    def __init__(self, index=None, sepal_length=None, sepal_width=None, petal_length=None, petal_width=None, label=None):
        self.index = index
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.label = label

    def create_from_string(self, string):
        attributes = string.split(',')

        for attribute in attributes:
            key, value = attribute.split(':')
            key = convert_camel_to_snake(key)
            setattr(self, key, value)

        self.normalise()

    def normalise(self):
        self.index = int(self.index)
        self.sepal_length = float(self.sepal_length)
        self.sepal_width = float(self.sepal_width)
        self.petal_length = float(self.petal_length)
        self.petal_width = float(self.petal_width)

        if self.label:
            self.label = int(self.label)

    @property
    def type(self):
        if self.label is None:
            return RecordType.TESTING
        else:
            return RecordType.TRAINING

    def as_dict(self):
        if self.type == RecordType.TESTING:
            return {'sepal_length': self.sepal_length, 'sepal_width': self.sepal_width, 'petal_length': self.petal_length,
                    'petal_width': self.petal_width}
        else:
            return {'sepal_length': self.sepal_length, 'sepal_width': self.sepal_width, 'petal_length': self.petal_length,
                    'petal_width': self.petal_width, 'label': self.label}

    def as_data_frame(self):
        return pd.DataFrame(self.as_dict(), index=[self.index])

    def __str__(self):
        if self.type == RecordType.TESTING:
            return f'TestingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width})'
        else:
            return f'TrainingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width}, label={self.label})'