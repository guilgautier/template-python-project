import pickle
import sys
from importlib import resources

import pandas

if sys.version_info < (3, 8):
    import pickle5 as pickle
else:
    import pickle


def load_mock_csv():
    return _load_csv("mock.csv")


def load_mock_pkl():
    return _load_pkl("mock.pkl")


def _load_csv(file_name):
    with resources.path("packagename.data", file_name) as path:
        df = pandas.read_csv(path)
    return df


def _load_pkl(file_name):
    data = resources.read_binary("packagename.data", file_name)
    dict_data = pickle.loads(data)
    # from_dict requires to convert single float values to array_like
    dict_data = {k: [v] for k, v in dict_data.items()}
    df = pandas.DataFrame.from_dict(dict_data)
    return df
