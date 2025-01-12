from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EmotionalUI"
    version: str = "0.1.0"

    class Config:
        env_file = "./app/.env"

settings = Settings()