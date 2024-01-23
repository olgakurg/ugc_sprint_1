from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings model for the application.
    """
    model_config: SettingsConfigDict = SettingsConfigDict(extra='ignore')
    project_name: str
    kafka_host: str
    kafka_port: int
    sentry_dsn: str
    sentry_enable: bool
    sentry_tracers_rate: float = 0.5
    sntry_profile_rate: float = 0.5


settings: Settings = Settings(_env_file='.env')
