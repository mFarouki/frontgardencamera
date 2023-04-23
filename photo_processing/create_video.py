import cv2
from photo_processing.constants import TO_PROCESS_DIR
from photo_processing.utilities import get_files


def create_video(output_path: str, fps=20.) -> None:
    processed_files = get_files(TO_PROCESS_DIR)
    frame = cv2.imread(str(processed_files[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for image in processed_files:
        video.write(cv2.imread(str(image)))

    cv2.destroyAllWindows()
    video.release()
