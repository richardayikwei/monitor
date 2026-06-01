"""
Check services running.

Checks services running on pc. service might includer servers
and other automated scripts
"""

import subprocess


def service_running(service_name: str) -> bool:
    """
    Check service to find out status.

    Args:
      service_name: str: the name of the service as represented in the computers system

    Returns:
        A boolean
    """
    result = subprocess.run(
        [
            "systemctl",
            "is-active",
            "--quiet",
            service_name,
        ]
    )
    
    return result.returncode == 0


def check_services(services: list[str]) -> list[str] | list[None]:
    """
    Run service_running function inputing various services.

    Args:
      services: list[str]: 

    Returns:
        An empty list or a list of services that are not running.
    """
    alerts = []

    for service in services:
        if not service_running(service):
            alerts.append(
                service
            )
    return alerts

def get_service_status(
    service_name: str
) -> str:
    """
    Get service status.

    Args:
        service_name: Systemd service name.

    Returns:
        "running" or "stopped"
    """
    if service_running(service_name):
        return "running"

    return "stopped"

def build_services_report(
    services: list[str]
) -> str:
    """
    Build a services status report.
    """

    lines = [
        "Services",
        "",
    ]

    for service in services:
        status = get_service_status(
            service
        )

        lines.append(
            f"{service}: {status}"
        )

    return "\n".join(lines)
