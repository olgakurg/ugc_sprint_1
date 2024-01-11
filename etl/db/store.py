from abc import ABC


class BaseStorage(ABC):

    async def write(self, table, data):
        pass
