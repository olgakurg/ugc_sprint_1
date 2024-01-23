from contextlib import asynccontextmanager
from typing import Generator

import sentry_sdk
from fastapi import FastAPI, Request, status, Header
from fastapi.responses import ORJSONResponse

from api.v1 import kafka_sender
from core.config import Settings
from core.log_middleware import LogMiddleware
from core.logger import logger
from db.kafka_settings import create_topics

settings = Settings()

if settings.sentry_enable:
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        traces_sample_rate=settings.sentry_tracers_rate,
        profiles_sample_rate=settings.sntry_profile_rate,
    )


@asynccontextmanager
async def lifespan(app: FastAPI) -> Generator:
    """
    Context manager for application lifespan.

    Args:
        app (FastAPI): The FastAPI application.

    Yields:
        None
    """
    create_topics(settings)
    yield


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


@app.middleware('http')
async def before_request(request: Request, call_next) -> ORJSONResponse:
    """
    Middleware to handle request before processing.

    Args:
        request (Request): The incoming request.
        call_next: The next middleware or endpoint to call.

    Returns:
        ORJSONResponse: The response.
    """
    response = await call_next(request)
    request_id = request.headers.get('X-Request-Id')
    if not request_id:
        return ORJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'detail': 'X-Request-Id is required'})
    return response


app.add_middleware(LogMiddleware)


@app.get("/sentry-debug")
async def trigger_error(x_request_id: str = Header(None)) -> float:
    """
    Endpoint to trigger an error for testing Sentry.

    Args:
        x_request_id (str, optional): The request ID. Defaults to None.

    Returns:
        float: The result of the division.
    """
    logger.info(f'get request id {x_request_id} to sentry-debug route')
    try:
        division_by_zero = 1 / 0
        logger.info(f'get request id {x_request_id} to sentry-debug route has a result {division_by_zero}')
        return division_by_zero
    except ZeroDivisionError as e:
        logger.error(f'{e} during handling {x_request_id}')


app.include_router(kafka_sender.router, prefix='/api/v1/send_to_kafka')