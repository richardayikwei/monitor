from datetime import datetime
from config import PROJECT_ROOT


HEARTBEAT_FILE = PROJECT_ROOT / "logs" / "heartbeat.txt"


def write_heartbeat():
    timestamp = datetime.now().isoformat()

    with open(HEARTBEAT_FILE, "w") as file:
        file.write(timestamp)
