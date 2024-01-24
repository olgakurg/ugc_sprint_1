import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse


from api.v1 import users_content_endpoint
from core.config import settings
from tools.log_middleware import LogMiddleware


app = FastAPI(
    title=settings.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.add_middleware(LogMiddleware)


@app.middleware('http')
async def before_request(request: Request, call_next):
    response = await call_next(request)
    request_id = request.headers.get('X-Request-Id')
    if not request_id:
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'detail': 'X-Request-Id is required'}
        )
    return response


app.include_router(users_content_endpoint.router,
                   prefix='/api/v1/user_content', tags=['user_content'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_config=None
    )
