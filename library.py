import requests

TOKEN_TELEGRAM = '6082820508:AAH6EmSXk0Sc9s37FOpVWiczH-l3X4wZHFA'
TELEGRAM_CHAT_ID = 942643203


def send_telegram_message(
        message: str,
        my_token: str = TOKEN_TELEGRAM,
        method: str = 'sendMessage',
):
    url = f"https://api.telegram.org/bot{my_token}/{method}"
    response = requests.post(
        url=url,
        data={'chat_id': TELEGRAM_CHAT_ID, 'text': message},
    )

    return response.json()
