from checks.disk import check_disk_usage
from checks.memory import check_memory_usage
from checks.services import check_services
from notifications.logger import write_alert


def run_checks():
    alerts = []

    alerts.extend(
        check_disk_usage()
    )

    alerts.extend(
        check_memory_usage()
    )
    
    alerts.extend(
        check_services(
            [
                "ssh",
                "tailscaled",
            ]
        )
    )

    return alerts

def main():
    alerts = run_checks()

    if not alerts:
        print("System healthy")
        return

    for alert in alerts:
        print(alert)
        write_alert(alert)

if __name__ == "__main__":
    main()
