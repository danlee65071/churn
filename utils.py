import zipfile
import os
import pathlib
import logging


logger = logging.getLogger("churn")


def extract(path_zip: str, dir_extract: str):
    with zipfile.ZipFile(path_zip, 'r') as zip_ref:
        zip_ref.extractall(dir_extract)


def exctract_data():
    try:
        zip = "p01_bank_data.zip"
        data_dir = pathlib.Path().resolve() / 'datasets'
        os.mkdir(data_dir)
        extract(zip, data_dir)
    except FileExistsError as e:
        logger.warning(e)
