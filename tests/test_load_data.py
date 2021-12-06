import pandas as pd
import pytest

from packagename.data.load_data import load_mock_csv, load_mock_pkl


@pytest.mark.parametrize("loader", [load_mock_csv, load_mock_pkl])
def test_smoke_load_data_returns_pandas_dataframe(loader):
    pands_dataframe = loader()
    assert isinstance(pands_dataframe, pd.DataFrame)
