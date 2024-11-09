# external imports
import pytest

# internal imports
from config import Settings, get_settings


@pytest.fixture()
def settings() -> Settings:
    return get_settings()


def test_settings(settings: Settings) -> None:
    assert isinstance(settings, Settings)
    assert isinstance(settings.APP_NAME, str)
    assert isinstance(settings.WANDB_API_KEY.get_secret_value(), str)
