import json
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from kafka3 import KafkaProducer

from api.v1 import kafka_producer
from core.config import Settings
from db import kafka
from db.kafka_settings import create_topics

settings = Settings()
logging.basicConfig(level=logging.INFO, filename="ugc_log.log", filemode="w")


@asynccontextmanager
async def lifespan(app: FastAPI):
    kafka.producer = KafkaProducer(bootstrap_servers=f'{settings.kafka_host}:{settings.kafka_port}',
                                   value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                   key_serializer=str.encode)
    create_topics(settings)
    yield


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(kafka_producer.router, prefix='/api/v1/send_to_kafka')
