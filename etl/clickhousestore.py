from aiochclient import ChClient
from aiohttp import ClientSession

from store import BaseStorage


class ClickHouse:

    def __init__(self, host, port):
        self.click_host = f"http://{host}:{port}"

    async def write(self, table, data):

        if data:
            column = data[0].keys()
            column = ", ".join(column)
            data = [tuple(row.values()) for row in data]

        else:
            return

        async with ClientSession() as s:
            client = ChClient(s, url=self.click_host)
            query = (
                f"INSERT INTO default.messages (*) "
                f"VALUES %s"
            )

            print(query)

            await client.execute(query, *data)
