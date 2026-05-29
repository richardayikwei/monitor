import requests


def send_message(
    token: str,
    chat_id: str,
    message: str,
) -> bool:

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
