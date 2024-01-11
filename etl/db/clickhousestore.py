import backoff
from aiochclient import ChClient, ChClientError
import aiohttp
from aiohttp import ClientSession

from config.settings import settings
from db.store import BaseStorage
from utils.processlogger import process_logger


class ClickHouse(BaseStorage):

    def __init__(self, host, port):
        self.click_host = f"http://{host}:{port}"

    @backoff.on_exception(
        backoff.expo,
        aiohttp.client_exceptions,
        logger=process_logger

    )
    async def write(self, data: list) -> bool | None:

        if not data:
            return

        async with ClientSession() as s:
            client = ChClient(s, url=self.click_host)
            query = f'INSERT INTO default.{settings.event_table} VALUES'

            try:
                await client.execute(query, *data)
                return True
            except ChClientError as e:
                process_logger.info(
                    'ClickHouse error %s' % e
                )
                return
