"""
Generate daily report

runs checks on various aspects of computer system
"""
import psutil
import subprocess
from datetime import datetime

def get_uptime():
    """
    Find how long computer has been running.


    Returns:
        The time the system has been running without reboot.
    """
    uptime_seconds = psutil.boot_time()

    uptime = datetime.now().timestamp() - uptime_seconds

    days = int(uptime // 86400)
    hours = int((uptime % 86400) // 3600)

    return f"{days}d {hours}h"


def service_status(service_name: str) -> str:
    """
    Check status of service
    Args:
      service_name: str: name of service

    Returns:
        String starting if service is running or down
    """
    result = subprocess.run(
        [
            "systemctl",
            "is-active",
            "--quiet",
            service_name,
        ]
    )

    return "Running" if result.returncode == 0 else "Down"

def generate_daily_report(services: list[str]) -> str:
    """
    Generate a services status report
    Args:
      services: list[str]: list containing services that should be checked 

    Returns:
        A string containing report
    """

    disk = psutil.disk_usage("/").percent
    memory = psutil.virtual_memory().percent

    report = [
        "Daily Server Report",
        "",
        f"Uptime: {get_uptime()}",
        f"Disk Usage: {disk}%",
        f"Memory Usage: {memory}%",
        "",
    ]

    for service in services:
        report.append(
            f"{service}: {service_status(service)}"
        )

    return "\n".join(report)
