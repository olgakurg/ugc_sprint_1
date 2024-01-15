from functools import lru_cache

from aiokafka import AIOKafkaProducer

kafka = AIOKafkaProducer | None


@lru_cache()
async def get_kafka_producer(settings) -> AIOKafkaProducer:
    yield kafka
