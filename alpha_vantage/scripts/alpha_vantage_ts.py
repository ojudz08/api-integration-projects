"""
    Fetch time series stock data from alpha vantage api.
    Date Created: March 5, 2026
"""

import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from report_logs import *
from user_config import get_user_config

# Initialize logger
logger = get_logs()

# Load environment variables
load_dotenv()

class AlphaVantageTimeSeries():

    def __init__(self, user_config):
        self.api_key = os.getenv("AV_API_KEY")
        self.user_config = user_config
        if not self.api_key:
            logger.error("API Key missing in .env file.")
            raise ValueError("API Key not found.")
        self.timeseries = TimeSeries(key=self.api_key, output_format='pandas')
        self.cryptocurrency = CryptoCurrencies(key=self.api_key, output_format='pandas') 

    def run_time_series(self):
        """ Parses user_config and executes the corresponding time series method automatically. """
        config = self.user_config.copy()
        method_name = config.pop('method_name', None)
        symbol = config.pop('symbol', None)

        if not method_name or not symbol:
            logger.error("Config missing 'method_name' or 'symbol'.")
            return None, None

        try:
            # Dynamically get the method from the alpha_vantage instance
            api_method = getattr(self.timeseries, method_name)
            
            logger.info(f"Initiating {method_name} for {symbol}...")
            data_df, meta_data = api_method(symbol=symbol, **config)
            
            logger.info(f"Successfully retrieved data for {symbol}.")
            return data_df, meta_data
        
        except ValueError as ve:
            logger.error(f"Invalid parameters for {symbol}: {ve}")
        except ConnectionError:
            logger.error("Network error: Could not connect to Alpha Vantage API.")
        except Exception as e:
            logger.error(f"Unexpected error for {symbol}: {e}", exc_info=True)

        return None, None

    def run_crypto_currencies(self):
        """Parse the user config for crypto currency"""
        test = self.cryptocurrency.get_crypto_intraday()

        return test



if __name__ == '__main__':
    user_config = get_user_config()

    av_client = AlphaVantageTimeSeries(user_config)
    data, metadata = av_client.run_time_series()

    file_input = input("Enter file name to save as csv: ").strip()
    file_path = Path(file_input)
    if file_path.suffix.lower() != '.csv':
        file_path = file_path.with_suffix('.csv')

    file_name = str(file_path)

    output_dir = Path(get_path()) / "data" / "output" / f"{file_name}"
    data_df = pd.DataFrame(data)
    data_df.to_csv(output_dir)