import torch

from config import Arguments


def test_default_values() -> None:
    """Test default values of Arguments class."""
    args = Arguments()
    assert args.name == "pytorch-template"
    assert args.device == "cuda" if torch.cuda.is_available() else "cpu"
