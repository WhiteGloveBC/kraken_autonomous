from core.template_header import *
from core.wrapper import wrap_execution
import requests

@wrap_execution
def call_llm(prompt, stream=False):
    url = os.getenv("LLM_API_URL", "http://localhost:8000/api/chat")
    headers = {"Content-Type": "application/json"}
    payload = {"prompt": prompt, "stream": stream}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return None
