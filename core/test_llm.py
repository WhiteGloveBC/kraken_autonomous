# FILE: test_llm.py

from llm_api_client import query_llm

response = query_llm("What is Kraken Autonomous?")
for line in response.iter_lines():
    print(line.decode())
    break  # just show first response line for quick test
