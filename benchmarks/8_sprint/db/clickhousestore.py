import asyncio

from aiochclient import ChClient
from aiohttp import ClientSession
from db.store import BaseStorage
from settings.settings import settings


class ClickHouse(BaseStorage):

    def __init__(self, host, port):
        self.click_host = f"http://{host}:{port}"

    async def async_write(self, data: list) -> bool | None:

        if not data:
            return

        async with ClientSession() as s:
            client = ChClient(s, url=self.click_host)
            query = f'INSERT INTO default.{settings.event_table} VALUES'

            await client.execute(query, *data)
            return True

    async def async_read(self, table: str, limit: int) -> list:

        query = f'SELECT * FROM default.{table} LIMIT {limit}'
        data = []
        async with ClientSession() as s:
            client = ChClient(s, url=self.click_host)

            async for row in client.iterate(query):
                data.append(tuple(row.values()))

        return data

    def write(self, data: list, table: str, column: list) -> bool | None:

        asyncio.run(self.async_write(data))

    def read(self, table: str, limit: int) -> list:
        data = asyncio.run(self.async_read(table, limit))
        return data
