import asyncio

import motor.motor_asyncio

from db.store import BaseStorage


class Mongo(BaseStorage):

    def __init__(self, host, port, database):

        self.client = motor.motor_asyncio.AsyncIOMotorClient(
            host, port
        )
        self.db = self.client[database]

    async def async_write(self, table: str, data: list) -> bool | None:

        collection = self.db[table]
        result = await collection.insert_many(data)

        return result

    async def async_read(self, table: str, limit: int) -> list:

        collection = self.db[table]
        cursor = collection.find({})

        res = await cursor.to_list(length=limit)

        return res

    async def async_count(
        self,
        table: str,
        fild_name: str,
        fild_value: str,
        relation_uuid: str = None
    ) -> int:

        collection = self.db[table]
        pipline = {
            fild_name: fild_value,
        }

        if relation_uuid:
            pipline['relation_uuid'] = relation_uuid

        res = await collection.count_documents(pipline)

        return res

    async def async_aggregate_func(self, table, pipline) -> list:

        collection = self.db[table]

        res = await collection.aggregate(pipline).to_list(None)

        return res
