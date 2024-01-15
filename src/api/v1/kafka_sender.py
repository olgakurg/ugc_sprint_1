from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from models import MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration
from services.kafka_service import KafkaService, get_kafka_service

router = APIRouter()


@router.post('/', status_code=HTTPStatus.OK)
async def send_to_kafka(payload: list[MovieProgress | MovieRes | FilterQuery | ClickElement | PageDuration],
                        kafka_service: KafkaService = Depends(get_kafka_service)):
    for event in payload:
        if isinstance(event, (MovieProgress, MovieRes, FilterQuery, ClickElement, PageDuration)):
            await kafka_service.send(event=event)
        else:
            raise HTTPException(status_code=400, detail="Invalid payload")

    return {'message': "OK"}
