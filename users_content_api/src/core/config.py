import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):

    project_name: str = 'test'

    uc_collections: str = 'users_content'
    uc_host: str = '0.0.0.0'
    uc_port: int = 27019
    uc_database: str = 'someDb'

    log_dir: str = './logs/'
    log_file: str = 'api.log'
    log_size: int = 2000
    log_backup_num: int = 5

    model_config = SettingsConfigDict(
        env_file='.env',
    )


settings = Settings()
