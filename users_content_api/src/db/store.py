from abc import ABC, abstractmethod


class BaseStorage(ABC):

    @abstractmethod
    def async_write(self, table, data):
        pass

    @abstractmethod
    def async_read(self, table, limit):
        pass
