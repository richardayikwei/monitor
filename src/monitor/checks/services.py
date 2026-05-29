import subprocess


def service_running(service_name: str):
    result = subprocess.run(
        [
            "systemctl",
            "is-active",
            "--quiet",
            service_name,
        ]
    )
    
    return result.returncode == 0


def check_services(services: list[str]):
    alerts = []

    for service in services:
        if not service_running(service):
            alerts.append(
                service
            )
    return alerts
