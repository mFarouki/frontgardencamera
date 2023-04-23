from datetime import datetime
from pathlib import Path


def get_files(directory: Path) -> list:
    return [x for x in directory.glob("**/*") if x.is_file()]


def log_info(message: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[INFO] {current_time}: {message}")
