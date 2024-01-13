from http import HTTPStatus

from db.kafka import get_kafka_producer
from db.kafka_settings import kafka_topics
from fastapi import APIRouter, Depends, HTTPException
from kafka3 import KafkaProducer
from models import MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def post_movie_progress(payload: list[MovieProgress | MovieRes | FilterQuery | ClickElement | PageDuration],
                              kafka_producer: KafkaProducer = Depends(get_kafka_producer)):
    for event in payload:
        if isinstance(event, (MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration)):
            kafka_producer.send(topic=kafka_topics[type(event).__name__],
                                value=event.value,
                                key=event.key)
        else:
            raise HTTPException(status_code=400, detail="Invalid payload")

    return {'message': "OK"}
