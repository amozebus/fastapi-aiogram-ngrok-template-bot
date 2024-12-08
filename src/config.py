"""Config for .env variables"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Model for .env variables validation"""

    BOT_API_TOKEN: str

    NGROK_URL: str

    model_config = SettingsConfigDict(extra="ignore")


settings = Settings()
