from photo_processing.constants import PROJECT_DIR
from photo_processing.construct_dataset import construct_dataset
from photo_processing.create_video import create_video
from photo_processing.process_images import process_images
from photo_processing.utilities import log_info

log_info("constructing dataset...")
construct_dataset()

log_info("processing images...")
process_images()

log_info("creating video...")
create_video(str(PROJECT_DIR / "front_garden_video.mp4"))
