import datetime

import pytest

from UnitTesting_in_Action import get_stock_data


# scope="class" tears down the fixture only at the end of the last test in the class, so we avoid rerunning this step.
@pytest.fixture(scope="class")
def stock_df():
    # We only want to pull this data once for each TestCase since it is an expensive operation
    df = get_stock_data('^DJI')
    return df


class TestGetStockData:

    def test_columns_present(self, stock_df):
        # ensures that the expected columns are all present
        assert "Open" in stock_df.columns
        assert "High" in stock_df.columns
        assert "Low" in stock_df.columns
        assert "Close" in stock_df.columns
        assert "Volume" in stock_df.columns

    def test_non_empty(self, stock_df):
        # ensures that there is more than one row of data
        assert len(stock_df.index) != 0

    def test_most_recent_within_week(self, stock_df):
        # most recent data was collected within the last week
        most_recent_date = pd.to_datetime(stock_df.index[0])
        assert (datetime.datetime.today() - most_recent_date).days <= 7
