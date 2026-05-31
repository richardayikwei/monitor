"""
Check disk usage.

Run a check on disk usage
"""

import psutil


def check_disk_usage(threshold: int) -> list[str] | list[None]:
    """
    Check whether disk usage exceeds a configured threshold.

    Args:
      threshold: int: Maximum allowed disk utilization percentage.
      threshold: int: 

    Returns:
      : An empty list or a list containing a string.

    """
    alerts = []

    usage = psutil.disk_usage("/")

    if usage.percent >= threshold:
        alerts.append(
                f"Disk usage critical: {usage.percent}%"
        )

    return alerts
