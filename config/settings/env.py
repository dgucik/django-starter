from enum import StrEnum
from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class DatabaseEngine(StrEnum):
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"

class Settings(BaseSettings):
    DEBUG: bool = False
    
    ALLOWED_HOSTS: list[str] | str = []

    SECRET_KEY: str

    DATABASE_ENGINE: DatabaseEngine = DatabaseEngine.SQLITE

    POSTGRES_DB: str | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: int | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


    @field_validator("ALLOWED_HOSTS", mode="before")
    @classmethod
    def parse_hosts(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(",") if x.strip()]
        return v


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()