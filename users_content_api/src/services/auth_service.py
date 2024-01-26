import uuid
from datetime import datetime, timedelta

from fastapi import Depends

from db.base_storage import BaseAsyncCache
from db.redis import RedisRepository
from services.base_token_service import BaseTokenService
from services.jwt_service import JwtService


class AuthorizationService(BaseTokenService):
    def __init__(
        self,
        token_service: JwtService,
        db: BaseAsyncCache
    ):
        self.tokenaser = token_service
        self.db = db

    async def check_access_token(self, acces_token):
        data = self.tokenaser.verify_token(acces_token)
        if data:
            exp_time = data['exp']
            if datetime.fromtimestamp(exp_time) >= datetime.utcnow():
                user_uuid = data['user_uuid']

                keys_logaut_tokens = await self.__get_logout_tokens(user_uuid)
                for key in keys_logaut_tokens:
                    token = await self.db.get(key=key)
                    if acces_token == token.decode('utf-8'):
                        return None
                return user_uuid
        return None

    async def __get_logout_tokens(self, user_uuid):
        tokens = await self.db.key_by_pattern(f'{user_uuid}:*')
        return tokens


def get_auth_service(
    db: BaseAsyncCache = Depends(RedisRepository),
    token_service: JwtService = Depends(JwtService)
) -> AuthorizationService:

    return AuthorizationService(token_service, db)
