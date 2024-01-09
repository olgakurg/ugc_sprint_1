import orjson
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from core.config import settings
from messtremmer.strimmer import Strimmer


class KafkaMesseger(Strimmer):
    def __init__(self, brocker_address):
        self.brocker_address = brocker_address

    async def write(self, topic: str, data: list, key: str):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.brocker_address,
            value_serializer=lambda m: orjson.dumps(
                m,
                default=lambda x: x.model_dump()
            ),
            key_serializer=lambda m: orjson.dumps(m)
        )
        await self.producer.start()

        try:
            await self.producer.send_and_wait(topic, key=key, value=data)
        except KafkaError:
            await self.producer.stop()


def get_kafka_producer() -> KafkaMesseger:
    brocker = settings.kafka_host + ':' + str(settings.kafka_port)
    return KafkaMesseger(brocker)
