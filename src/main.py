
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import kafka_sender
from core.config import Settings
from db.kafka_settings import create_topics

settings = Settings()
logging.basicConfig(level=logging.INFO, filename="ugc_log.log", filemode="w")


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_topics(settings)
    yield


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(kafka_sender.router, prefix='/api/v1/send_to_kafka')
