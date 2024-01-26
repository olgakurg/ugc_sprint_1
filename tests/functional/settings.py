import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class TestSettings(BaseSettings):

    service_url: str = '0.0.0.0'
    uc_collections: str = 'users_content'
    uc_host: str = '0.0.0.0'
    uc_port: int = 27019
    uc_database: str = 'someDb'

    access_token_expires_in: int = 30
    jwt_secret_key: str = 'JWT_SECRET_KEY'
    jwt_algorithm: str = 'JWT_ALGORITHM'

    model_config = SettingsConfigDict(
        env_file='.env.tests',
    )


settings = TestSettings()
