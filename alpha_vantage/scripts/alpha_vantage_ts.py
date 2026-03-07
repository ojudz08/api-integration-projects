"""
    Fetch time series stock data from alpha vantage api.
    Date Created: March 5, 2026
"""

import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from report_logs import get_logs
from user_config import get_user_config

# Initialize logger from get_logs function
logger = get_logs()

# Load environment variables
load_dotenv()


class AlphaVantageTimeSeries():

    def __init__(self):
        self.api_key = os.getenv("AV_API_KEY")
        if not self.api_key:
            logger.error(f"API Key missing in .env file.")
            raise ValueError("API Key not found. Please set your Alpha Vantage API KEY in your .env file.")
        self.timeseries = TimeSeries(key=self.api_key, output_format='pandas')
        test = self.timeseries.get
    

    def _execute_api_call(self, method_name: str, symbol: str, **kwargs):
        """ Internal helper that handles API calling logic and error handling.
        """
        if not symbol:
            logger.error(f"Execution failed: 'symbol' is required for {method_name}.")
            raise ValueError(f"The 'symbol' argument is required for {method_name}.")

        try:
            # Dynamically get the method from the alpha_vantage instance
            api_method = getattr(self.timeseries, method_name)
            
            logger.info(f"Initiating {method_name} call for ticker {symbol}...")
            data_df, meta_data = api_method(symbol=symbol, **kwargs)
            
            logger.info(f"Successfully retrieved data for {symbol}.")
            return data_df, meta_data

        except ValueError as ve:
            logger.error(f"Invalid parameters for {symbol}: {ve}")
        except ConnectionError:
            logger.error("Network error: Could not connect to Alpha Vantage API.")
        except Exception as e:
            logger.error(f"Unexpected error for {symbol}: {e}", exc_info=True)
        
        return None, None


    def ts_intraday(self, **kwargs):
        """ Get the historical intraday OHLCV time series of the equity specified.
            Args:
                **kwargs: Dictionary containing:
                    symbol (str): The stock ticker (e.g., 'AAPL')
                    interval (str): Time interval between 2 consecutive data points (e.g., '1min', '5min', '15min', '30min', '60min')
                    adjusted (bolean): True - Stock data adjustment for historical split and dividend events; False -  returns as traded intraday values.
                    extended_hours (boolean): True - Include both the regular and extended trading hours (pre and post market from 4:00am to 8:00pm); False - Includes only trading hours from 9:30am to 4:00pm US ET
                    month (str): Month parameter in YYYY-MM format to fetch a specific month in history
                    outputsize (str): 'compact' or 'full'. Defaults to 'compact'
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_intraday', symbol, **kwargs)


    def ts_daily(self, **kwargs):
        """ Get the daily time series OHLCV of the equity defined. Returns a dataframe format and its metadata
            Args:
                **kwargs: Dictionary containing:
                    symbol (str): The stock ticker (e.g., 'AAPL')
                    outputsize (str): 'compact' or 'full'. Defaults to 'compact'
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_daily', symbol, **kwargs)


    def ts_daily_adj(self, **kwargs):
        """ Get the adjusted time series close values OHLCV of the equity defined. Returns a dataframe format and its metadata
            Args:
                **kwargs: Dictionary containing:
                    symbol (str): The stock ticker (e.g., 'AAPL')
                    outputsize (str): 'compact' or 'full'. Defaults to 'compact'
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_daily_adjusted', symbol, **kwargs)


    def ts_weekly(self, **kwargs):
        """ definition here
            Args:
                **kwargs: Dictionary containing symbol (str): The stock ticker (e.g., 'AAPL')
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_weekly', symbol, **kwargs)
    

    def ts_weekly_adj(self, **kwargs):
        """ definition here
            Args:
                **kwargs: Dictionary containing symbol (str): The stock ticker (e.g., 'AAPL')
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_weekly_adjusted', symbol, **kwargs)


    def ts_monthly(self, **kwargs):
        """ definition here
            Args:
                **kwargs: Dictionary containing symbol (str): The stock ticker (e.g., 'AAPL')
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_monthly', symbol, **kwargs)


    def ts_monthly_adj(self, **kwargs):
        """ definition here
            Args:
                **kwargs: Dictionary containing symbol (str): The stock ticker (e.g., 'AAPL')
        """

        symbol = kwargs.pop('symbol', None)
        return self._execute_api_call('get_monthly_adjusted', symbol, **kwargs)



if __name__ == '__main__':
    timeseries = AlphaVantageTimeSeries()

    config = get_user_config()

    print(config)
    #data, metadata = timeseries.ts_weekly(**config)

    # data, metadata = get_user_config()

    # if data is not None:
    #     print(f"\nSuccessfully fetched {len(data)} rows of data.")
    #     print(data)
