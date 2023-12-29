import asyncio


from transport import Transport
from clickhousestore import ClickHouse
from sourcekafka import KafkaMesseger
from config.settings import settings


if __name__ == '__main__':
    store = ClickHouse(settings.db_address, settings.db_port)
    source = KafkaMesseger(f'{settings.bus_address}:{settings.bus_port}')
    etl = Transport(source=source, storage=store, topics=['messages'])

    asyncio.run(etl.create_stream())
