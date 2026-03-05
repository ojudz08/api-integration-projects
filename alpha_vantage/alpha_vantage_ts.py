"""
    Fetch time series stock data from alpha vantage api.
    Date Created: March 5, 2026
"""

import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries


# Load environment variables
load_dotenv()


def ts_intraday():
    pass


def ts_daily(symbol):
    """Get the daily time series in dataframe format and it's metadata"""
    ts = TimeSeries(key=api_key, output_format='pandas')
    data_df, meta_data = ts.get_daily(symbol=symbol)
    return data_df, meta_data


def ts_daily_adj():
    pass


def ts_weekly():
    pass


def ts_weekly_adj():
    pass


def ts_monthly():
    pass


def ts_monthly_adj():
    pass


api_key = os.getenv("AV_API_KEY")

sym = "WDC"

test = ts_daily(sym)

print(test[0])
print(test[1])
    