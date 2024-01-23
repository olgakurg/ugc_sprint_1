import logging
from functools import lru_cache
from typing import Type, Union

import orjson
from aiokafka import AIOKafkaProducer
from core.config import settings
from db.kafka_settings import kafka_topics
from models import MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration


@lru_cache()
def get_kafka_service() -> Type['KafkaService']:
    """
    Function to get KafkaService class.

    Returns:
        Type[KafkaService]: The KafkaService class.
    """
    return KafkaService


class KafkaService:
    """
    Kafka service for sending events.
    """
    @staticmethod
    async def send(event: Union[MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration]) -> None:
        """
        Send an event to Kafka.

        Args:
            event (Union[MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration]): The event to send.

        Returns:
            None
        """
        try:
            producer = AIOKafkaProducer(
                bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_port}',
                value_serializer=lambda m: orjson.dumps(
                    m,
                    default=lambda x: x.model_dump()
                ),
                key_serializer=lambda m: orjson.dumps(m)
            )

            await producer.start()
            await producer.send_and_wait(
                topic=kafka_topics[type(event).name],
                value=event.value,
                key=event.key
            )
            await producer.stop()
        except Exception as e:
            logging.error(e)
