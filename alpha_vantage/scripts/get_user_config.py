# def timeseries_args(get_method):
#     if get_method == 'intraday': return self.ts_intraday(kwargs)
#     elif get_method == 'daily': return self.ts_daily(kwargs)
#     elif get_method == 'daily adjusted': return self.ts_daily_adj(kwargs)
#     elif get_method == 'weekly': return self.ts_weekly(kwargs)
#     elif get_method == 'weekly adjusted': return self.ts_weekly_adj(kwargs)
#     elif get_method == 'monthly': return self.ts_monthly(kwargs)
#     elif get_method == 'monthly adjusted': return self.ts_monthly_adj(kwargs)
#     else:
#         logger.error(f"No method {method_name}. Check your input.")


# def get_user_config():
#     """Dynamic function to capture runtime variables."""
#     print("\n--- Stock Data Fetcher ---")
#     symbol = input("Enter Ticker Symbol (e.g., TSLA): ").upper()
#     get_method = input("Enter what time series data - intraday, daily, daily adjusted, weekly, weekly adjusted, monthly or monthly adjusted: ")
    

#     return {"symbol": symbol, "method": get_method}



from pathlib import Path


# Save logs to file and prints them
log_dir = Path("./logs")
test = Path(__file__).resolve()
print(test)

# log_dir.mkdir(exist_ok=True)