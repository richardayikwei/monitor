from config import load_config

from reports.daily import (
    generate_daily_report,
)

from notifications.report_logger import (
    write_daily_report,
)
from notifications.telegram import send_message
from dotenv import load_dotenv
import os


load_dotenv()

def main() -> None:
    config = load_config()

    report = generate_daily_report(
        config["services"]
    )

    print(report)

    write_daily_report(report)

    send_message(
        os.environ["TELEGRAM_BOT_TOKEN"],
        os.environ["TELEGRAM_CHAT_ID"],
        report
    )

if __name__ == "__main__":
    main()
