from config import load_config

from reports.daily import (
    generate_daily_report,
)

from notifications.report_logger import (
    write_daily_report,
)


def main() -> None:
    config = load_config()

    report = generate_daily_report(
        config["services"]
    )

    print(report)

    write_daily_report(report)


if __name__ == "__main__":
    main()
