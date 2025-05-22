from pydantic import Field
from pydantic_settings import BaseSettings

from app.config.env_config import DatabaseConfig, RedisConfig


class Settings(BaseSettings):
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)


settings = Settings()