from report_logs import get_logs

# Initialize logger from get_logs function
logger = get_logs()


def config_method_name(get_method):
    words = get_method.lower().split()
    method_name = "get_" + "_".join(words)
    
    method_name_list = ["get_intraday", "get_daily", "get_daily_adjusted", "get_weekly", "get_weekly_adjusted", "get_monthly", "get_monthly_adjusted"]

    if method_name not in method_name_list:
        err_msg = "Method name incorrect. Check your input."
        logger.error(f"{err_msg}")
        raise ValueError(err_msg)

    return method_name



def config_intraday(get_method):
    method_name = config_method_name(get_method)
    symbol = input("Enter ticker symbol (e.g., TSLA): ").upper()
    interval = input("Enter time interval between 2 consecutive data points (e.g., 1min, 5min, 15min, 30min, 60min): ")
    adjusted = input("Enter 'True' (Data adjustment for historical split & dividend events) or 'False' (As-traded intraday values): ")
    extended_hours = input("Enter 'True' (both regular and extended trading hours from 4:00am to 8:00pm) or 'False' (regular trading hours from 9:30am to 4:00pm US ET): ")
    outputsize = input("Enter 'compact' (latest 100 data points) or 'full' (full-length 20+ yrs historical data): ")
    
    config_args = { "method_name": method_name,
                    "symbol": symbol, 
                    "interval": interval, 
                    "adjusted": adjusted,
                    "extended_hours": extended_hours,
                    "outputsize": outputsize    }
    return config_args


def config_daily(get_method):
    method_name = config_method_name(get_method)
    symbol = input("Enter ticker symbol (e.g., TSLA): ").upper()
    outputsize = input("Enter 'compact' (latest 100 data points) or 'full' (full-length 20+ yrs historical data): ")
    
    config_args = { "method_name": method_name,
                    "symbol": symbol, 
                    "outputsize": outputsize    }
    return config_args
    

def config_weekly_monthly(get_method):
    method_name = config_method_name(get_method)
    symbol = input("Enter ticker symbol (e.g., TSLA): ").upper()

    config_args = { "method_name": method_name,
                    "symbol": symbol    }
    return config_args


def get_user_config():
    """Dynamic function to capture runtime variables."""
    print("\n--- Stock Data Fetcher ---")
    # symbol = input("Enter Ticker Symbol (e.g., TSLA): ").upper()
    get_method = input("Enter what time series data - intraday, daily, daily adjusted, weekly, weekly adjusted, monthly or monthly adjusted: ")

    if get_method == 'intraday':
        config_kwargs = config_intraday()
    elif get_method == 'daily' or get_method == 'daily adjusted':
        config_kwargs = config_daily()
    else:
        config_kwargs = config_weekly_monthly()     

    return config_kwargs
