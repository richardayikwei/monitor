from datetime import datetime

from config import PROJECT_ROOT

REPORT_FILE = (
    PROJECT_ROOT
    / "logs"
    / "daily_report.log"
)


def write_daily_report(
    report: str,
) -> None:

    REPORT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().isoformat()

    with open(REPORT_FILE, "a") as file:
        file.write(
            f"\n[{timestamp}]\n"
        )
        file.write(report)
        file.write("\n")
