"""
Logs daily report.

Saves daily report to file
"""

from datetime import datetime

from monitor.config import PROJECT_ROOT

REPORT_FILE = (
    PROJECT_ROOT
    / "logs"
    / "daily_report.log"
)


def write_daily_report(
    report: str,
) -> None:
    """
    Save report to daily_report.log.

    Args:
      report: str: status of system components and services 
    """
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
