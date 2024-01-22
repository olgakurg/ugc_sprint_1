from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='ignore')
    project_name: str
    kafka_host: str
    kafka_port: int
    sentry_dsn: str
    sentry_enable: bool
    sentry_tracers_rate: int = 0.5
    sntry_profile_rate: int = 0.5


settings = Settings(_env_file='.env')
