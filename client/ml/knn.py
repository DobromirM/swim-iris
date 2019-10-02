from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier


class KNN:

    def __init__(self, n_neighbors=2):
        self.model = KNeighborsClassifier(n_neighbors)

    def fit(self, train_data):
        train_y = train_data['label']
        train_x = train_data.drop('label', axis=1)

        self.model.fit(train_x, train_y)

    def predict(self, data):
        return self.model.predict(data).astype(int)

    def measure_accuracy(self, data):
        test_y = data['label']
        test_x = data.drop('label', axis=1)
        pred_y = self.model.predict(test_x).astype(int)

        accuracy = metrics.accuracy_score(test_y, pred_y)
        return accuracy
