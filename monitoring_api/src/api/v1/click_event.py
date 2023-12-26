from http import HTTPStatus

from db.kafka import get_kafka_producer
from db.kafka_settings import kafka_topics
from fastapi import APIRouter, Depends
from kafka3 import KafkaProducer
from models import ClickElement

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def post_click_event(payload: ClickElement,
                           kafka_producer: KafkaProducer = Depends(get_kafka_producer)):
    kafka_producer.send(topic=kafka_topics[ClickElement],
                        value={
                            'event_time': str(payload.event_time)
                        },
                        key=f'{payload.user_id}+{payload.element_id}')

    return {'message': "OK"}
