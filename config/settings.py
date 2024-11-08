# external imports
from functools import lru_cache

from pydantic import ConfigDict, SecretStr
from pydantic_settings import BaseSettings

# internal imports


class Settings(BaseSettings):
    """Base settings class for the application."""

    # Secret key for the application
    WANDB_API_KEY: SecretStr

    # General settings
    APP_NAME: str = "Pytorch Template"

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False,
        secrets_dir=None,
    )


@lru_cache
def get_settings() -> Settings:
    """Get the settings object."""
    return Settings()
