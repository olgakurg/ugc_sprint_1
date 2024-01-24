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

    model_config = SettingsConfigDict(
        env_file='.env',
    )


settings = Settings()
