# external imports
from nvitop import Device

# internal imports
from src.main import main


def test_main() -> None:
    main()


def test_devices() -> None:
    devices = Device.all()
    for device in devices:
        processes = device.processes()
        sorted_pids = sorted(processes.keys())

        print(device)  # noqa: T201
        print(f"  - Fan speed:       {device.fan_speed()}%")  # noqa: T201
        print(f"  - Temperature:     {device.temperature()}C")  # noqa: T201
        print(f"  - GPU utilization: {device.gpu_utilization()}%")  # noqa: T201
        print(f"  - Total memory:    {device.memory_total_human()}")  # noqa: T201
        print(f"  - Used memory:     {device.memory_used_human()}")  # noqa: T201
        print(f"  - Free memory:     {device.memory_free_human()}")  # noqa: T201
        print(f"  - Processes ({len(processes)}): {sorted_pids}")  # noqa: T201
        for pid in sorted_pids:
            print(f"    - {processes[pid]}")  # noqa: T201
        print("-" * 120)  # noqa: T201
