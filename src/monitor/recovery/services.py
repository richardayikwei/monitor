"""
Restart service.

Restarts service that has failed
"""

import subprocess


def restart_service(
    service_name: str,
) -> bool:
    """
    Restart service.

    Args:
      service_name: str: the name of the service that needs restarting. 

    Returns:
        boolean as to the status of the restarted service.
    """
    result = subprocess.run(
        [
            "systemctl",
            "restart",
            service_name,
        ]
    )

    return result.returncode == 0
