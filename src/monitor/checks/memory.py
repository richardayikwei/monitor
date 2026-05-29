import psutil


def check_memory_usage(threshold: int):
    alerts = []

    memory = psutil.virtual_memory()

    if memory.percent >= threshold:
        alerts.append(
                f"Memory usage critcal: {memory.percent}%"
                )
    return alerts
