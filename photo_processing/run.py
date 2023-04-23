from photo_processing.construct_dataset import construct_dataset
from photo_processing.create_video import create_video
from photo_processing.process_images import process_images
from photo_processing.constants import SCRIPT_DIR

construct_dataset()
process_images()
create_video(str(SCRIPT_DIR / "front_garden_video.mp4"))
