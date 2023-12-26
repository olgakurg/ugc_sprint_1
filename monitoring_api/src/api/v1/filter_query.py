from http import HTTPStatus

from db.kafka import get_kafka_producer
from db.kafka_settings import kafka_topics
from fastapi import APIRouter, Depends
from kafka3 import KafkaProducer
from models import FilterQuery

router = APIRouter()


# TODO придумать что-то с ключами для фильтров запроса (они опциональные, а надо что-то реконструируемое)
@router.post('/', status_code=HTTPStatus.OK)
async def post_page_view(payload: FilterQuery,
                         kafka_producer: KafkaProducer = Depends(get_kafka_producer)):
    kafka_producer.send(topic=kafka_topics[FilterQuery],
                        value={
                            'duration': payload.duration,
                            'event_time': str(payload.event_time)
                        },
                        key=f'{payload.user_id}+{payload.page_id}')

    return {'message': "OK"}
