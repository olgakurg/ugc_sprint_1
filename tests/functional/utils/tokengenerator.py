from uuid import UUID
from datetime import datetime, timedelta

from utils.jwt_service import JwtService

from settings import settings


def token_generate(
    login: str,
    role: UUID,
    user_uuid: UUID
):

    expiration_time = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expires_in
    )
    playload = {
        'login': str(login),
        'user_uuid': str(user_uuid),
        'role': str(role),
        'exp': expiration_time,
        'type': 'access'
    }

    jwt_service = JwtService()
    access_token = jwt_service.create_token(data=playload)

    return access_token
