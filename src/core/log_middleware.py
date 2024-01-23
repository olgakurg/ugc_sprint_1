from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from .logger import logger


class LogMiddleware(BaseHTTPMiddleware):
    """
    Middleware for logging incoming requests and responses.
    """

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """
        Process and log the incoming request and response.

        Args:
            request (Request): The incoming request.
            call_next (RequestResponseEndpoint): The next middleware or endpoint to call.

        Returns:
            Response: The response.
        """
        response = await call_next(request)
        logger.info(
            "Incoming request",
            extra={
                "req": {"method": request.method, "url": str(request.url)},
                "res": {"status_code": response.status_code},
            },
        )
        return response
