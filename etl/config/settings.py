from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    db_address: str = '0.0.0.0'
    db_port: int = 8123

    bus_address: str = '0.0.0.0'
    bus_port: int = 29392
    topics_str: str = "movies_progress"
    batch_size: int = 100

    topics: list | None = None


settings = Settings()
settings.topics = settings.topics_str.split(',')
