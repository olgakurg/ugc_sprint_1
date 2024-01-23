from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    clickhuse_address: str = '0.0.0.0'
    clickhuse_port: int = 8123
    vertica_address: str = '0.0.0.0'
    vertica_port: int = 5433
    vertica_user: str = 'dbadmin'
    vertica_db_name: str = 'docker'
    mongo_port: int = 5433
    mongo_host: str = 'dbadmin'
    mongo_db_name: str = 'docker'

    event_table: str = 'ugc_db'


settings = Settings()
