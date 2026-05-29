import subprocess


def restart_service(
    service_name: str,
) -> bool:
    result = subprocess.run(
        [
            "systemctl",
            "restart",
            service_name,
        ]
    )

    return result.returncode == 0
