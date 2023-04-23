import cv2

from photo_processing.constants import (PROCESSED_PHOTOS_DIR, RAW_PHOTOS_DIR,
                                        TO_PROCESS_DIR)
from photo_processing.utilities import get_files

NOISE_IMAGE = RAW_PHOTOS_DIR / "background_noise.jpg"


def denoise_image(image_file) -> None:
    image = cv2.imread(str(image_file))
    image -= cv2.imread(str(NOISE_IMAGE))
    denoised_imaged = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite(str(PROCESSED_PHOTOS_DIR / image_file.name), denoised_imaged)


def process_images():
    files_to_process = get_files(TO_PROCESS_DIR)
    assert len(files_to_process) > 0, f"we expect at least one file in {TO_PROCESS_DIR}"
    for file in files_to_process:
        denoise_image(file)
