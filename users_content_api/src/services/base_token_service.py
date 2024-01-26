from abc import ABC, abstractclassmethod


class BaseTokenService(ABC):

    @abstractclassmethod
    async def check_access_token(self, acces_token: str):
        pass
