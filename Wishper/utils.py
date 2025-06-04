# utils.py

import json
import os
from datetime import datetime

CONFIG_PATH = "config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return {
            "secret_mode": False,
            "auto_delete": False,
            "auto_reply": False,
            "dark_mode": True
        }
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)

def log_message(sender, message):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"[{time}] {sender}: {message}")

def auto_response():
    responses = [
        "I'm currently unavailable. Talk soon!",
        "Auto-response: Please leave a message.",
        "Whisper-bot says hi 👋"
        "Set Up Custom Message"
        "Thanks To Developer Ankan"
    ]
    return responses[datetime.now().second % len(responses)]

def format_message(message):
    return message.strip()

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
