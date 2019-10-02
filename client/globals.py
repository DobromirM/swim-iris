from ml.datasets import Dataset
from ml.knn import KNN

TRAINING_DATA = Dataset()
GROUND_TRUTH_DATA = Dataset(['../data/test/iris_test_1.csv', '../data/test/iris_test_2.csv'], 'index')
ML = KNN(n_neighbors=3)
