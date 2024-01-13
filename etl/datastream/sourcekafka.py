import json
import backoff
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError


from datastream.sourcemes import SouceMessager
from utils.processlogger import process_logger


class KafkaMesseger(SouceMessager):
    def __init__(self, brocker):
        self.brocker = brocker

    @backoff.on_exception(
        backoff.expo,
        KafkaConnectionError,
        logger=process_logger

    )
    async def read(self, source):
        consumer = AIOKafkaConsumer(
            source,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            key_deserializer=lambda m: m.decode('utf-8'),
            bootstrap_servers=self.brocker,
        )
        await consumer.start()

        return consumer
