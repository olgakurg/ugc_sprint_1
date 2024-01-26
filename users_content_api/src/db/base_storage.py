from abc import ABC, abstractmethod


class BaseAsyncCache(ABC):
    @abstractmethod
    async def get(self, key: str, **kwargs):
        pass

    @abstractmethod
    async def set(self, key: str, value: str, expire: int, **kwargs):
        pass

    @abstractmethod
    async def delete(self, key: str, value: str, expire: int, **kwargs):
        pass

    @abstractmethod
    async def key_by_pattern(self, patern):
        pass
