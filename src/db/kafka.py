from contextlib import asynccontextmanager
from typing import AsyncGenerator

from aiokafka import AIOKafkaProducer


@asynccontextmanager
async def get_kafka_producer(settings) -> AsyncGenerator[AIOKafkaProducer, None]:
    """
    Asynchronous context manager for getting a Kafka producer.

    Args:
        settings: The settings for the Kafka producer.

    Yields:
        AIOKafkaProducer: The Kafka producer.
    """
    kafka = AIOKafkaProducer(bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_port}')
    await kafka.start()
    try:
        yield kafka
    finally:
        await kafka.stop()
