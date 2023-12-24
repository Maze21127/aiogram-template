from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BOT_")
    TOKEN: SecretStr


class Settings(BaseSettings):
    bot: BotSettings() = BotSettings()


def get_settings() -> Settings:
    return Settings()
