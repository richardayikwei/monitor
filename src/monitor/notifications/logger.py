"""
Logs alerts

Logs services that fail
logs restart of services failure
"""

from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
LOG_FILE = PROJECT_ROOT / "logs" / "monitor.log"


def write_alert(message: str) -> None:
    """
    Write alerts to monitor.log file
    Args:
      message: str: the name of the alert that failed 

    Returns:

    """
    LOG_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().isoformat()

    with open(LOG_FILE, "a") as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )
