from telegram.ext import (
    Application,
    CommandHandler,
)

from monitor.bot.handlers import (
    help_command,
    memory_command,
    disk_command,
    services_command
)
from dotenv import load_dotenv
import os

load_dotenv()



def main() -> None:
    """Start Telegram bot."""

    app = (
        Application.builder()
        .token(os.environ["TELEGRAM_BOT_TOKEN"] )
        .build()
    )

    app.add_handler(
        CommandHandler(
            "help",
            help_command,
        )
    )

    app.add_handler(
        CommandHandler(
            "memory",
            memory_command,
        )
    )

    app.add_handler(
        CommandHandler(
            "disk",
            disk_command,
        )
    )

    app.add_handler(
                CommandHandler(
                "services",
                services_command,
        )
    )

    app.run_polling()


if __name__ == "__main__":
    main()
