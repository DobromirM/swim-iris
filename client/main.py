import asyncio

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

from client import run
from ml.datasets import Dataset

if __name__ == '__main__':
    # record = Record()
    # record.create_from_string('index:100,sepalLength:6.3,sepalWidth:3.3,petalLength:6,petalWidth:2.5,label:2')
    #
    # print(GROUND_TRUTH_DATA)
    # pass

    # add_training_data(pd.DataFrame(record.as_dict(), index=[record.index]))
    # print(get_training_data())
    #
    # model = KNeighborsClassifier(n_neighbors=3)
    #
    #
    # model.fit(train_x_s, train_y_s)
    # prediction = model.predict(test_x_p)
    # print('The accuracy of KNN is:', metrics.accuracy_score(prediction, test_y_p))

    # test = Dataset(['../data/test/iris_test_1.csv', '../data/test/iris_test_2.csv'], 'index')
    # train = Dataset(
    #     ['../data/train/iris_train_1.csv'], 'index')
    #
    # train_y = train.data['label']
    # train_x = train.data.drop('label', axis=1)
    #
    # test_y = test.data['label']
    # test_x = test.data.drop('label', axis=1)
    #
    # model = KNeighborsClassifier(n_neighbors=3)
    # model.fit(train_x, train_y)
    # pred_y = model.predict(test_x)
    #
    # accuracy = metrics.accuracy_score(test_y, pred_y)
    # print(accuracy)


    uri = "ws://localhost:9001"

    agents = list()
    agents.append(['/training/1', 'data'])
    agents.append(['/training/2', 'data'])
    agents.append(['/training/3', 'data'])
    agents.append(['/training/4', 'data'])

    agents.append(['/testing/1', 'data'])
    agents.append(['/testing/2', 'data'])

    asyncio.get_event_loop().run_until_complete(run(uri, agents))
