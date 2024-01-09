from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore')
    project_name: str
    kafka_host: str = "localhost"
    kafka_port: int = 29392


settings = Settings(_env_file='.env')
