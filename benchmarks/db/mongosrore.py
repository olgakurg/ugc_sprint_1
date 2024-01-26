import asyncio

import motor.motor_asyncio


from settings.settings import settings
from db.store import BaseStorage


class Mongo(BaseStorage):

    def __init__(self, host, port, database):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            host, port, io_loop=loop
        )
        self.db = self.client[database]

    async def async_write(self, table: str, data: list) -> bool | None:

        collection = self.db[table]
        result = await collection.insert_many(data)

        return result

    def write(self, table: str, column: list, data: list) -> bool | None:

        documents = [dict(zip(column, item)) for item in data]

        loop = self.client.get_io_loop()
        res = loop.run_until_complete(self.async_write(table, documents))

        return res

    async def async_read(self, table: str, limit: int) -> list:

        collection = self.db[table]
        cursor = collection.find({})

        res = await cursor.to_list(length=limit)

        return res

    def read(self, table: str, limit: int) -> list:

        loop = self.client.get_io_loop()
        res = loop.run_until_complete(self.async_read(table, limit))

        return res
