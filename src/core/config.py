from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore')
    project_name: str
    kafka_host: str
    kafka_port: int
    sentry_dsn: str


settings = Settings(_env_file='.env')
