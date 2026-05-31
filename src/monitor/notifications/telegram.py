"""
Send message to telegram

Sends message to telegram bot
"""

import requests


def send_message(
    token: str,
    chat_id: str,
    message: str,
) -> bool:
    """
    Send https request to telegram bot containing message payload
    Args:
      token: str: Telegram bot token
      chat_id: str: Telegram bot id 
      message: str: message being sent to bot

    Returns:
        boolean of response

    """

    url = (
        f"https://api.telegram.org/"
        f"bot{token}/sendMessage"
    )

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": message,
        },
        timeout=10,
    )

    return response.ok
