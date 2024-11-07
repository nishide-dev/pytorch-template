# external imports
import torch
import torch.version as torch_version

# internal imports


def main() -> None:
    print(f"PyTorch version: {torch.__version__}")  # noqa: T201
    print(f"CUDA version: {torch_version.cuda}")  # noqa: T201
    print(f"CUDNN version: {torch.backends.cudnn.version()}")  # noqa: T201
    print("-" * 120)  # noqa: T201


if __name__ == "__main__":
    main()
