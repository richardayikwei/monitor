"""
Check memory usage

Runs a memory check against configured threshold
"""

import psutil


def check_memory_usage(threshold: int) -> list[str] | list[None]:
    """Check whether memory usage exceeds a configured thereshold

    Args:
      threshold: int: Maximum allowed memory utilization percentage.
      threshold: int: 

    Returns:
      : An alert in a list or and empty list if no alert

    """
    alerts = []

    memory = psutil.virtual_memory()

    if memory.percent >= threshold:
        alerts.append(
                f"Memory usage critcal: {memory.percent}%"
                )
    return alerts
