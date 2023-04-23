import os
from pathlib import Path

SCRIPT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
RAW_PHOTOS_DIR = DATA_DIR / "input_data"
TO_PROCESS_DIR = DATA_DIR / "to_process"
PROCESSED_PHOTOS_DIR = DATA_DIR / "processed_data"
