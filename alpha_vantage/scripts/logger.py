import logging
from pathlib import Path

# def get_log_path():
#     """Returns the root directory of the project based on a marker file."""
#     current_path = Path(__file__).resolve()
    
#     for parent in current_path.parents:
#         if (parent / ".env").exists() or (parent / ".git").exists():
#             return parent
            
#     return Path.cwd()


# def logger():
#     # Save logs to file and prints them
#     log_dir = Path("./logs")
#     log_dir.mkdir(exist_ok=True)

#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s -- %(message)s",
#         datefmt="%Y-%m-%d %I:%M %p",
#         handlers=[
#             logging.FileHandler(log_dir / f"logs_{date.today()}.log"),
#             logging.StreamHandler()
#         ]
#     )
#     log_result = logging.getLogger(__name__)

#     return log_result


# Path("./logs") / "news_fetcher_logs.log")

log_dir = Path(".alpha_vantage", "logs")
print(log_dir)

log_dir.mkdir(parents=True, exist_ok=True)