from core.template_header import *
from core.wrapper import wrap_execution
import json

@wrap_execution
def parse_module_list(response):
    if not response:
        print("[PARSER] Empty response from LLM.")
        return []

    try:
        data = json.loads(response)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "modules" in data:
            return data["modules"]
        else:
            print("[PARSER] Unexpected structure:", data)
            return []
    except json.JSONDecodeError:
        # fallback: split raw string into lines
        lines = response.strip().splitlines()
        modules = [line.strip("-• ").strip() for line in lines if line.strip()]
        return modules
