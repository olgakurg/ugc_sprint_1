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
    mongo_port: int = 27019
    mongo_host: str = '0.0.0.0'
    mongo_db_name: str = 'someDb'
    pg_host: str = '0.0.0.0'
    pg_port: int = 5432
    pg_db_name: str = 'benchmark'
    pg_user: str = 'postgres'
    pg_password: str = 'postgres'

    event_table: str = 'events'


settings = Settings()
