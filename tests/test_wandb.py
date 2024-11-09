# external imports
import wandb

# internal imports
from config import get_settings


def test_wandb_login() -> None:
    settings = get_settings()
    assert settings.WANDB_API_KEY.get_secret_value() is not None

    assert wandb.login(key=settings.WANDB_API_KEY.get_secret_value())
