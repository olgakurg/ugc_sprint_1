from abc import ABC


class Strimmer(ABC):

    async def write(self, topic: str, data: list) -> None:
        pass
