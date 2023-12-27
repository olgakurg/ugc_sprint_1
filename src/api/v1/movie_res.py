from http import HTTPStatus

from db.kafka import get_kafka_producer
from db.kafka_settings import kafka_topics
from fastapi import APIRouter, Depends
from kafka3 import KafkaProducer
from models import MovieRes

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def post_movie_res(payload: MovieRes,
                         kafka_producer: KafkaProducer = Depends(get_kafka_producer)):
    kafka_producer.send(topic=kafka_topics[MovieRes],
                        value=payload.get_value(),
                        key=str(payload.get_key()))

    return {'message': "OK"}
