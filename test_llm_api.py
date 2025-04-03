# FILE: llm_api_client.py

import requests

def query_llm(prompt, model="command-a:latest", session_id="kraken", include_memory=True):
    url = "http://localhost:8000/api/chat"
    payload = {
        "prompt": prompt,
        "model": model,
        "session_id": session_id,
        "include_memory": include_memory
    }
    response = requests.post(url, json=payload, stream=True)
    return response

