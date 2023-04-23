import os
from pathlib import Path

SCRIPT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
PROJECT_DIR = SCRIPT_DIR.parent
RAW_PHOTOS_DIR = PROJECT_DIR / "input_data"
TO_PROCESS_DIR = PROJECT_DIR / "to_process"
PROCESSED_PHOTOS_DIR = PROJECT_DIR / "processed_data"
