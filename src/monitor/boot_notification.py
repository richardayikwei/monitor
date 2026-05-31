"""
Send boot notifications

Send boot notifications on reboot or boot of server or device
"""

from datetime import datetime
import os
import socket

from dotenv import load_dotenv

from notifications.telegram import (
    send_message,
)

load_dotenv()


def main() -> None:
    """
    get hostname, time and send notifications to telegram
    """
    hostname = socket.gethostname()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    message = (
        "🟢 Server Booted\n\n"
        f"Hostname: {hostname}\n"
        f"Time: {timestamp}"
    )

    send_message(
        os.environ["TELEGRAM_BOT_TOKEN"],
        os.environ["TELEGRAM_CHAT_ID"],
        message,
    )


if __name__ == "__main__":
    main()
