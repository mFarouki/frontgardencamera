from pathlib import Path

import cv2
import numpy as np

from photo_processing.constants import (PROCESSED_PHOTOS_DIR, PROJECT_DIR,
                                        RAW_PHOTOS_DIR, TO_PROCESS_DIR)
from photo_processing.utilities import get_files

# Image taken with no input, to subtract as background noise
NOISE_IMAGE = PROJECT_DIR / "resources" / "background_noise.jpg"


def denoise_image(image_file: Path, noise: np.ndarray) -> None:
    image = cv2.imread(str(image_file)).astype(np.float64)
    image -= noise
    denoised_imaged = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(str(PROCESSED_PHOTOS_DIR / image_file.name), denoised_imaged)


def process_images():
    noise = cv2.imread(str(NOISE_IMAGE)).astype(np.float64)
    files_to_process = get_files(TO_PROCESS_DIR)
    assert len(files_to_process) > 0, f"we expect at least one file in {TO_PROCESS_DIR}"
    for file in files_to_process:
        denoise_image(file, noise)
