import logging
from pathlib import Path
from datetime import date


def get_log_path():
    """Returns the root directory of the alpha vantage project"""
    current_path = Path(__file__).resolve()
    
    for parent in current_path.parents:
        if (parent / ".env").exists() or (parent / ".git").exists():
            return parent


def get_logs():
    """Save logs to file with date and time stamp"""
    log_dir = Path(get_log_path()) / "logs"
    log_dir.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s -- %(message)s",
        datefmt="%Y-%m-%d %I:%M %p",
        handlers=[
            logging.FileHandler(log_dir / f"logs_{date.today()}.log"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)