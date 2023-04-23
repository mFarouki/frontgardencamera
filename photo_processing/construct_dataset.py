import datetime as dt
import re
import shutil
from pathlib import Path
from urllib.request import urlopen

from photo_processing.constants import RAW_PHOTOS_DIR, TO_PROCESS_DIR
from photo_processing.utilities import get_files

CAMBRIDGE_SUN_TIMES_URL = (
    "https://www.ukweathercams.co.uk/sunrise_sunset_times.php?id=6518"
)

MIN_DATETIME = dt.datetime(year=2023, month=4, day=20, hour=19, minute=30)
INPUT_FILE_FORMAT = "%Y-%m-%d_%H-%M-%S"


def assert_dt_format(dt_text: str, error_msg: str, dt_format="%Y-%m-%d") -> dt:
    try:
        formatted_dt = dt.datetime.strptime(dt_text, dt_format)
    except ValueError:
        raise ValueError(error_msg)
    return formatted_dt


def get_sun_times(date_text: str) -> list:
    """
    Returns a list of sunrise and sunset in Cambridge on a given date
    :param date_text: date to query in format YYYY-MM-DD
    :return: list of sunrise and sunset times as HH:MM
    """
    date_to_query = assert_dt_format(
        dt_text=date_text, error_msg="incorrect date_text format; must be YYYY-MM-DD"
    )
    page = urlopen(f"{CAMBRIDGE_SUN_TIMES_URL}&dt={date_to_query.strftime('%d-%m-%Y')}")
    page_html = page.read().decode("utf-8")

    # regular expression to find sunrise and sunset (highly specific to site queried)
    sun_times_re = 'sunrise = ".*",\n.*sunset = ".*",'
    raw_sun_times_text = re.search(sun_times_re, page_html, re.IGNORECASE).group()

    return re.findall(r"\d{2}:\d{2}", raw_sun_times_text)


def get_file_info(file: Path) -> (str, dt, str):
    file_name = file.stem
    file_dt = assert_dt_format(
        dt_text=file_name,
        error_msg=f"file {file_name} did not match format {INPUT_FILE_FORMAT}",
        dt_format=INPUT_FILE_FORMAT,
    )
    file_date = file_dt.strftime("%Y-%m-%d")
    return file_name, file_dt, file_date


def construct_dataset():
    """
    Selects images front frontgardencamera that can be used to create a video. Excludes images taken before camera is a
    consistent position and also images taken before sunrise or after sunset. Constructs dataset to be processed before
    combining into a video.
    :return: None
    """
    TO_PROCESS_DIR.mkdir(exist_ok=True)
    input_files = get_files(RAW_PHOTOS_DIR)
    sun_times = {}
    for file in input_files:
        file_name, file_dt, file_date = get_file_info(file)
        if file_name < MIN_DATETIME.strftime(INPUT_FILE_FORMAT):
            continue
        if file_date not in sun_times:
            sun_times[file_date] = [
                dt.datetime.strptime(f"{file_date} {sun_time}:01", "%Y-%m-%d %H:%M:%S")
                for sun_time in get_sun_times(file_date)
            ]
        date_sunrise, date_sunset = sun_times[file_date][0], sun_times[file_date][1]
        if file_dt < date_sunrise or file_dt > date_sunset:
            continue
        shutil.copy(file, TO_PROCESS_DIR / file.name)
