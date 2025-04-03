from datetime import datetime
import os
import requests

def reflect(message, level="REFLECT"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{level}] {timestamp} — {message}"
    print(formatted)
    send_pushover_alert(formatted)

def send_pushover_alert(message):
    user_key = os.getenv("PUSHOVER_USER_KEY")
    api_token = os.getenv("PUSHOVER_API_TOKEN")

    if not user_key or not api_token:
        return  # Silent fail if keys not set

    try:
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": api_token,
                "user": user_key,
                "message": message
            },
            timeout=5
        )
    except Exception as e:
        print(f"[REFLECT] Failed to send Pushover alert: {e}")
