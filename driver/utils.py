from pathlib import Path


def assert_target_existed(target_file: Path):
    if target_file.exists():
        return None
    raise FileNotFoundError(f"{target_file.name}")
