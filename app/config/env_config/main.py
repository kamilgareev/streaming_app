from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    DB: str

    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
        extra="ignore",
        env_file='.env'
    )

    @property
    def DB_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@"
                f"{self.HOST}:{self.PORT}/{self.DB}")


class RedisConfig(BaseSettings):
    HOST: str
    PORT: int
    CACHE_DB_NUM: int = Field(default=0)

    model_config = SettingsConfigDict(
        env_prefix="REDIS_",
        extra="ignore",
        env_file='.env'
    )

    @property
    def CACHE_URL(self) -> str:
        return f"redis://{self.HOST}:{self.PORT}/{self.CACHE_DB_NUM}"
