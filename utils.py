import zipfile
import os
import pathlib
import logging

from sklearn.base import BaseEstimator, TransformerMixin



logger = logging.getLogger("churn")


class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attributes_name):
        self.attributes_name = attributes_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attributes_name].values


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
