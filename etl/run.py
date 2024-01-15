import asyncio

from transport import Transport
from db.clickhousestore import ClickHouse
from datastream.sourcekafka import KafkaMesseger
from config.settings import settings


if __name__ == '__main__':
    store = ClickHouse(settings.db_address, settings.db_port)
    source = KafkaMesseger(f'{settings.bus_address}:{settings.bus_port}')
    etl = Transport(source=source, storage=store, topics=settings.topics)

    asyncio.run(etl.create_stream())
