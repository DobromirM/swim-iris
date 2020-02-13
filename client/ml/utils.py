from enum import Enum

IRIS_NAMES = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']


class IrisLabels(Enum):
    setosa: 1
    versicolor: 2
    virginica: 3

    @classmethod
    def get_name(self, label):
        return IRIS_NAMES[label]
