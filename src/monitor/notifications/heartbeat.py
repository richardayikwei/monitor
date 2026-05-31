"""
Write to heartbeat file.

Saves the last time the monitoring software run
"""

from datetime import datetime
from config import PROJECT_ROOT


HEARTBEAT_FILE = PROJECT_ROOT / "logs" / "heartbeat.txt"


def write_heartbeat():
    """Save last run of monitoring software to heartbeat.txt."""
    timestamp = datetime.now().isoformat()

    with open(HEARTBEAT_FILE, "w") as file:
        file.write(timestamp)
