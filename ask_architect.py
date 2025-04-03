from core.template_header import *
from core.wrapper import wrap_execution, with_reflection
from core.architect_input import get_prompt
from core.architect_request import send_prompt_to_llm, stream_prompt_to_llm
from core.architect_parser import parse_module_list
from core.module_factory import create_module
from core.template_footer import *
import sys

@with_reflection("Arch request started")
@wrap_execution
def prompt_architect(stream=True, interactive=True):
    prompt = get_prompt(interactive=interactive)
    if not prompt:
        return

    response = stream_prompt_to_llm(prompt) if stream else send_prompt_to_llm(prompt)
    if not response:
        return

    modules = parse_module_list(response)
    if not modules:
        return

    for mod in modules:
        create_module(mod)

if __name__ == "__main__":
    stream = True
    interactive = True

    if "--no-stream" in sys.argv:
        stream = False
    if "--no-interactive" in sys.argv:
        interactive = False

    prompt_architect(stream=stream, interactive=interactive)
