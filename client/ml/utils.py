import re
from enum import Enum

IRIS_NAMES = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']


class IrisLabels(Enum):
    setosa: 1
    versicolor: 2
    virginica: 3

    @classmethod
    def get_name(self, label):
        return IRIS_NAMES[label]


def convert_camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
