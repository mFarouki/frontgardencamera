from photo_processing.constants import PROJECT_DIR
from photo_processing.construct_dataset import construct_dataset
from photo_processing.create_video import create_video
from photo_processing.process_images import process_images

construct_dataset()
process_images()
create_video(str(PROJECT_DIR / "front_garden_video.mp4"))
