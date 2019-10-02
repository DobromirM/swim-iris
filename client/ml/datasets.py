import pandas as pd


class Dataset:

    def __init__(self, files=None, index=None):

        self.data = pd.DataFrame()

        if files:
            for file in files:
                self.data = self.data.append(pd.read_csv(file, index_col=index))

    @property
    def size(self):
        return len(self.data)

    def add_data(self, data):
        self.data = self.data.append(data)

    def add_from_file(self, file):
        self.data = self.data.append(pd.read_csv(file))
