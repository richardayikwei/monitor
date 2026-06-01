"""
Daily report.

generate report
send report to telegram
"""

from monitor.config import load_config

from monitor.reports.daily import (
    generate_daily_report,
)

from monitor.notifications.report_logger import (
    write_daily_report,
)
from monitor.notifications.telegram import send_message
from dotenv import load_dotenv
import os


load_dotenv()

def main() -> None:
    """Generate report and send via telegram."""
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
