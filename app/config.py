from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    EVENTS_HANDLER: SecretStr
    LOGGING_MODE: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()