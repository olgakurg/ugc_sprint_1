from http import HTTPStatus

from db.kafka import get_kafka_producer
from db.kafka_settings import kafka_topics
from fastapi import APIRouter, Depends
from kafka3 import KafkaProducer
from models import MovieProgress

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def post_movie_progress(payload: MovieProgress,
                              kafka_producer: KafkaProducer = Depends(get_kafka_producer)):
    kafka_producer.send(topic=kafka_topics[MovieProgress],
                        value={'movie_progress': payload.movie_progress,
                               'movie_length': payload.movie_len,
                               'event_time': str(payload.event_time)
                               },
                        key=f'{payload.user_id}+{payload.movie_id}')

    return {'message': "OK"}
