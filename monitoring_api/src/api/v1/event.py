from http import HTTPStatus
from datetime import datetime

# from db.kafka import get_kafka_producer
# from db.kafka_settings import kafka_topics

from fastapi import APIRouter, Depends, Query, Body
# from kafka3 import KafkaProducer

from models import Event
from messtremmer.asynckafka import KafkaMesseger, get_kafka_producer


router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def post_event(
    data: list[Event],
    kafka_producer: KafkaMesseger = Depends(get_kafka_producer)
):

    await kafka_producer.write(topic="events",
                               data=data,
                               key=datetime.now()
                               )

    return {'message': "OK"}
