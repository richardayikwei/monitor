import psutil


def check_disk_usage(threshold: int):
    alerts = []

    usage = psutil.disk_usage("/")

    if usage.percent >= threshold:
        alerts.append(
                f"Disk usage critical: {usage.percent}%"
        )

    return alerts
