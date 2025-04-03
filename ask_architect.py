from core.architect_input import get_prompt
from core.architect_request import send_prompt_to_llm
from core.architect_parser import parse_module_list
from core.wrapper import with_reflection

@with_reflection
def prompt_architect():
    prompt = get_prompt()
    raw = send_prompt_to_llm(prompt)
    modules = parse_module_list(raw)

    if not modules:
        print("[ARCHITECT] No modules parsed.")
    else:
        print(f"[ARCHITECT] Parsed {len(modules)} modules:")
        for m in modules:
            print(f" - {m['filename']}: {m['description']}")

    return modules

if __name__ == "__main__":
    prompt_architect()
