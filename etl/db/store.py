from abc import ABC


class BaseStorage(ABC):

    async def write(self, table: str, data: list) -> bool | None:
        pass
