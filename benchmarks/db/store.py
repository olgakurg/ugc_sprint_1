from abc import ABC


class BaseStorage(ABC):

    def write(self, table, column, data):
        pass

    def read(self, table, limit):
        pass
