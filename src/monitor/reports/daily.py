import psutil
import subprocess
from datetime import datetime

def get_uptime():
    uptime_seconds = psutil.boot_time()

    uptime = datetime.now().timestamp() - uptime_seconds

    days = int(uptime // 86400)
    hours = int((uptime % 86400) // 3600)

    return f"{days}d {hours}h"


def service_status(service_name: str):
    result = subprocess.run(
        [
            "systemctl",
            "is-active",
            "--quiet",
            service_name,
        ]
    )

    return "Running" if result.returncode == 0 else "Down"

def generate_daily_report(services: list[str]):

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
