from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    RATE_LIMIT_WINDOW: int = 60
    RATE_LIMIT_MAX: int = 3

settings = Settings()