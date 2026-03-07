from report_logs import get_logs

logger = get_logs()

# Mapping methods to their specific requirements
VALID_METHODS = {
    "intraday": ["interval", "adjusted", "extended_hours", "outputsize"],
    "daily": ["outputsize"],
    "daily adjusted": ["outputsize"],
    "weekly": [],
    "weekly adjusted": [],
    "monthly": [],
    "monthly adjusted": []
}


def config_method_name(raw_method):
    """Validates the method name."""
    clean_method_name = raw_method.lower().strip()
    if clean_method_name not in VALID_METHODS:
        err_msg = f"Method '{clean_method_name}' is incorrect. Check your input."
        logger.error(err_msg)
        raise ValueError(err_msg)
    
    # Convert method with "get_" i.e. "get_daily_adjusted"
    return f"get_{'_'.join(clean_method_name.split())}"


def get_user_config():
    """Single dynamic function to capture all necessary variables."""
    print("\n--- Stock Data Fetcher ---")

    raw_method = input(f"Enter time series ({', '.join(VALID_METHODS.keys())}): ").lower().strip()
    method_name = config_method_name(raw_method)
    
    # Every method requires a symbol
    config_args = {
        "method_name": method_name,
        "symbol": input("Enter ticker symbol (e.g., TSLA): ").upper().strip()
    }

    # Determine what are the needed arguments based on the method
    required_args = VALID_METHODS.get(raw_method, [])

    if "interval" in required_args:
        config_args["interval"] = input("Enter interval (1min, 5min, 15min, 30min, 60min): ")
    
    if "adjusted" in required_args:
        config_args["adjusted"] = input("Adjusted for dividends? (True/False): ")
        
    if "extended_hours" in required_args:
        config_args["extended_hours"] = input("Include extended hours? (True/False): ")

    if "outputsize" in required_args:
        config_args["outputsize"] = input("Enter outputsize ('compact' or 'full'): ")

    return config_args