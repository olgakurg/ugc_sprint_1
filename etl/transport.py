import asyncio

from sourcemes import SouceMessager
from store import BaseStorage

from config.settings import settings
from sourcemes import SouceMessager


class Transport:
    def __init__(
        self,
        source: SouceMessager,
        storage: BaseStorage,
        topics: list
    ):
        self.source = source
        self.storage = storage
        self.topics = topics

    async def streammer(self, topic: str):
        data_stream = []

        async for msg in await self.source.read(topic):
            data_stream.append(msg.value)

            # if len(data_stream) >= settings.batch_size:
            await self.storage.write(topic, data_stream)

    async def create_stream(self):
        workers = []

        for topic in self.topics:
            task = self.streammer(topic)
            workers.append(task)

        await asyncio.gather(* workers)
