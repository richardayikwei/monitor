"""
Run Monitor

check disk usage
check memory usage
check services
send telegram message
log reports
"""

from checks.memory import check_memory_usage
from checks.services import check_services
from notifications.logger import write_alert
from config import load_config
from checks.disk import check_disk_usage
from notifications.heartbeat import write_heartbeat
from recovery.services import restart_service
from notifications.telegram import send_message
from dotenv import load_dotenv
import os


load_dotenv()

def run_checks() -> list[str] | list[None]:
    """
    Run System checks

    Returns:
        Am empty list or a list of alerts showing the abnormal System variables
    """
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

def main() -> None:
    """
    Run all checks
    """
    alerts = run_checks()
    write_heartbeat()

    if alerts:
        send_message(
            os.environ["TELEGRAM_BOT_TOKEN"],
            os.environ["TELEGRAM_CHAT_ID"],
            "Monitor check failed"
        )

 
    if not alerts:
        print("System healthy")
        return
    
    for alert in alerts:
        print(alert)
        write_alert(alert)

        restart = restart_service(alert)

        if restart:
            write_alert(
                f"Restart successful: {alert}"
            )
        else:
            write_alert(
                    f"Restart failed: {alert}"
            )

if __name__ == "__main__":
    main()
