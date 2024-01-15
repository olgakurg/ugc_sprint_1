import asyncio
from uuid import uuid4
from datetime import datetime

from aiokafka.structs import ConsumerRecord


from datastream.sourcemes import SouceMessager
from utils.processlogger import process_logger
from config.settings import settings
from db.store import BaseStorage


class Transport:

    required = ['user_id', 'event_time', 'event_type']

    def __init__(
        self,
        source: SouceMessager,
        storage: BaseStorage,
        topics: list
    ):
        self.source = source
        self.storage = storage
        self.topics = topics

    async def streammer(self, topic: str) -> None:
        data_stream = []

        process_logger.info(
            'producer for topic %s has been started' % topic
        )

        async for msg in await self.source.read(topic):

            process_logger.info(
                'received new message from topic %s' % topic
            )

            data = self.message_trnsform(msg)
            data_stream.append(data)

            if len(data_stream) >= settings.batch_size:
                status = await self.storage.write(data_stream)

                if status:
                    process_logger.info(
                        '%s messages saved in database' % len(data_stream)
                    )
                    data_stream.clear()

    async def create_stream(self) -> None:
        workers = []

        for topic in self.topics:
            task = self.streammer(topic)
            workers.append(task)
            process_logger.info(
                'create consumer for topic %s' % topic
            )

        await asyncio.gather(* workers)

    def message_trnsform(self, msg: ConsumerRecord) -> tuple:
        data = msg.value

        user_id = data.get('user_id')
        event_time = data.get('event_time')
        if event_time:
            event_time = event_time.split('.')[0]
        event_type = msg.key

        values = {}

        for key, value in data.items():
            if key in self.required:
                continue
            else:
                values[key] = value

        row = (uuid4(), user_id, values, event_time, event_type)

        row = () if None in row else row

        return row
