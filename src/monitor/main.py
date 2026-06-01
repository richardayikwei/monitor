from monitor.checks.memory import check_memory_usage
from monitor.checks.services import check_services
from monitor.notifications.logger import write_alert
from monitor.config import load_config
from monitor.checks.disk import check_disk_usage
from monitor.notifications.heartbeat import write_heartbeat
from monitor.recovery.services import restart_service
from monitor.notifications.telegram import send_message
from dotenv import load_dotenv
import os


load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def run_checks():
    """ """
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
    """ """
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
