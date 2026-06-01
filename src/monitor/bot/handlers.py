from telegram import Update
from telegram.ext import ContextTypes
import os
from monitor.checks.memory import get_memory_usage
from monitor.checks.disk import get_disk_usage
from dotenv import load_dotenv

load_dotenv()


def authorized(update: Update) -> bool:
    """Check whether the sender is authorized."""

    return (
        str(update.effective_chat.id)
        == str(os.environ["TELEGRAM_CHAT_ID"])
    )

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Display available bot commands."""
    
    if not authorized(update):
        return
    
    await update.message.reply_text(
        """
Available Commands

/help
/memory
/disk
"""
    )


async def memory_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Display current memory usage."""

    if not authorized(update):
        return

    usage = get_memory_usage()

    await update.message.reply_text(
        f"Memory Usage: {usage}%"
    )


async def disk_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """Display current disk usage."""
    
    if not authorized(update):
        return

    usage = get_disk_usage()

    await update.message.reply_text(
        f"Disk Usage: {usage}%"
    )
