from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    pair = data.get('pair', 'Unknown Pair')
    signal = data.get('signal', 'No Signal')
    entry_time = data.get('entry_time', 'N/A')
    price = data.get('price', 'N/A')

    message = f"*Pocket Option Signal*\n" \
              f"Pair: {pair}\n" \
              f"Signal: {signal}\n" \
              f"Entry Time: {entry_time}\n" \
              f"Price: {price}"

    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage', data={{
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }})

    return 'OK', 200
