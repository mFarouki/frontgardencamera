from pathlib import Path


def get_files(directory: Path) -> list:
    return [x for x in directory.glob("**/*") if x.is_file()]
