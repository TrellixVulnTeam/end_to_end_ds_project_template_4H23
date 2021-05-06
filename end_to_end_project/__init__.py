__version__ = '0.1.0'

"""Initialize script."""
from .get_data import (
    fetch_housing_data, load_housing_data, split, pickle_data
)


def get_data_script():
    fetch_housing_data()
    data = load_housing_data()
    train_set, test_set = split(data)
    pickle_data(train_set, 'train_set.pkl')
    pickle_data(test_set, 'test_set.pkl')
