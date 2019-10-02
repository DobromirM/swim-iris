from utils.data_utils import convert_camel_to_snake
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

    @property
    def type(self):
        if self.label is None:
            return RecordType.TESTING
        else:
            return RecordType.TRAINING

    def __str__(self):
        if self.type == RecordType.TESTING:
            return f'TestingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width})'
        else:
            return f'TrainingRecord(index={self.index}, sepal_length={self.sepal_length}, sepal_width={self.sepal_width}, petal_length={self.petal_length}, petal_width={self.petal_width}, label={self.label})'
