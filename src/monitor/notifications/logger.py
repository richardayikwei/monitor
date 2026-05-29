from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
LOG_FILE = PROJECT_ROOT / "logs" / "monitor.log"


def write_alert(message: str):
    LOG_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    timestamp = datetime.now().isoformat()

    with open(LOG_FILE, "a") as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )
