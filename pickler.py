import pickle


class PickleBuilder:

    def __init__(self, pickle_file):
        self.file_name = pickle_file

    def create_pickle(self):
        pass

    def open_pickle(self):
        pass

class ConcretePickleBuilder:

    def __init__(self, pickle_file):
        self.file_name = pickle_file

    def create_pickle(self):
        file = open('pickle_file.pickle', 'wb')
        pickle.dump(self.file_name, file)
        file.close()
        print('file pickled')

    def open_pickle(self):
        self.file_name = open('pickle_file.pickle', 'rb')
        print('file opened')
        print(self.file_name)
