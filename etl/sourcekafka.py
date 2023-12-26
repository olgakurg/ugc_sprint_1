import json
import asyncio
from aiokafka import AIOKafkaConsumer

from sourcemes import SouceMessager


class KafkaMesseger(SouceMessager):
    def __init__(self, brocker):
        self.brocker = brocker

    async def read(self, source):
        consumer = AIOKafkaConsumer(
            source,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            bootstrap_servers=self.brocker,
        )
        await consumer.start()

        return consumer
