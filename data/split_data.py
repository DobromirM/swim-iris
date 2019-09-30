import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('iris.csv')
    data['label'] = data['label'].astype("category").cat.codes

    data = data.sample(frac=1)

    data[0:25].to_csv('train/iris_train_1.csv', index_label='index')
    data[25:50].to_csv('train/iris_train_2.csv', index_label='index')
    data[50:75].to_csv('train/iris_train_3.csv', index_label='index')
    data[75:100].to_csv('train/iris_train_4.csv', index_label='index')

    data[100:125].to_csv('test/iris_test_1.csv', index_label='index')
    data[125:150].to_csv('test/iris_test_2.csv', index_label='index')
