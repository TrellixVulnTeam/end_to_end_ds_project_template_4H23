import os
import tarfile
from urllib import request
import pandas as pd
from sklearn.model_selection import train_test_split
import config
from . import helpers

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
RAW_DATA_PATH = os.path.join(config.base_dir, 'data/raw')
RAW_DATA_DIRECTORY = 'data/raw'
TEST_SIZE = 0.2
RANDOM_STATE = 1


def fetch_housing_data(data_url=HOUSING_URL, path=RAW_DATA_PATH):
    """Gets housing data from URL and saves in data folder"""
    # Create data directory if doesn't exist
    try:
        os.makedirs(path, exist_ok=True)
        print(
            f"Directory '{path}' created successfully, or already exists")
    except OSError as error:
        print(f"Directory '{path}' can not be created, Error: {error}")

    # Create path for file
    file_path = os.path.join(path, 'housing.tgz')

    # Get data and copy to file path
    request.urlretrieve(data_url, file_path)
    # urllib.request.urlretrieve(data_url, file_path)

    # Open, extract and close file
    with tarfile.open(file_path) as housing_tgz:
        housing_tgz.extractall(path=path)


def load_housing_data(housing_path=RAW_DATA_PATH):
    """Loads housing data to pandas dataframe"""
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


def split(dataframe):
    train_set, test_set = train_test_split(
        dataframe,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )
    return train_set, test_set


def pickle_data(dataframe, pickle_file_name):
    pickle_path = os.path.join(RAW_DATA_PATH, pickle_file_name)
    dataframe.to_pickle(pickle_path)
