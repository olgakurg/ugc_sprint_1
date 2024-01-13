from abc import ABC


class SouceMessager(ABC):

    async def read(self, source) -> list:
        pass
