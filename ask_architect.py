from core.template_header import *
from core.wrapper import with_reflection, wrap_execution
from core.architect_input import get_prompt
from core.architect_request import send_prompt_to_llm, stream_prompt_to_llm
from core.architect_parser import parse_module_list
from core.module_factory import create_module

@with_reflection("Arch request started")
@wrap_execution
def prompt_architect(stream=True, interactive=True):
    prompt = get_prompt(interactive=interactive)
    response = stream_prompt_to_llm(prompt) if stream else send_prompt_to_llm(prompt)

    # ✅ Ensure function is actually called
    modules = parse_module_list(response)

    if not isinstance(modules, list):
        print("[ARCHITECT] parse_module_list did not return a list.")
        return

    for mod in modules:
        create_module(mod)

if __name__ == "__main__":
    stream = "--no-stream" not in sys.argv
    interactive = "--no-interactive" not in sys.argv
    prompt_architect(stream=stream, interactive=interactive)
