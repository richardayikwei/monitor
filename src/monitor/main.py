from checks.memory import check_memory_usage
from checks.services import check_services
from notifications.logger import write_alert
from config import load_config
from checks.disk import check_disk_usage
from notifications.heartbeat import write_heartbeat


def run_checks():
    config = load_config()
    alerts = []

    alerts.extend(
        check_disk_usage(config["disk_threshold"])
    )

    alerts.extend(
        check_memory_usage(config["memory_threshold"])
    )
    
    alerts.extend(
        check_services(
            config["services"]
        )
    )

    return alerts

def main():
    alerts = run_checks()
    write_heartbeat()

    if not alerts:
        print("System healthy")
        return

    for alert in alerts:
        print(alert)
        write_alert(alert)

if __name__ == "__main__":
    main()
