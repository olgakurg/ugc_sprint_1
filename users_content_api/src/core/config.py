import os
from logging import config as logging_config
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):

    project_name: str = 'test'

    uc_collections: str = 'users_content'
    uc_host: str = '0.0.0.0'
    uc_port: int = 27019
    uc_database: str = 'someDb'
    redis_host: str = '127.0.0.1'
    redis_port: int = 6379
    redis_password: str = 'REDIS_PASSWORD'

    jwt_secret_key: str = 'JWT_SECRET_KEY'
    jwt_algorithm: str = 'JWT_ALGORITHM'

    model_config = SettingsConfigDict(
        env_file='.env',
    )


settings = Settings()
