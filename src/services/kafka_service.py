import logging
from functools import lru_cache

import orjson
from aiokafka import AIOKafkaProducer
from core.config import settings
from db.kafka_settings import kafka_topics
from models import MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration


@lru_cache()
def get_kafka_service():
    return KafkaService


class KafkaService:
    @staticmethod
    async def send(event: MovieProgress | MovieRes | FilterQuery | ClickElement | PageDuration):
        producer = AIOKafkaProducer(bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_port}',
                                    value_serializer=lambda m: orjson.dumps(
                                        m,
                                        default=lambda x: x.model_dump()
                                    ),
                                    key_serializer=lambda m: orjson.dumps(m)
                                    )

        await producer.start()
        try:
            await producer.send_and_wait(topic=kafka_topics[type(event).__name__],
                                         value=event.value,
                                         key=event.key)
        except Exception as e:
            logging.error(e)
            raise e
        finally:
            await producer.stop()
