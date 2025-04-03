from core.template_header import *
from core.wrapper import wrap_execution
from core.file_parser import get_arg

@wrap_execution
def get_prompt(interactive=True):
    if interactive:
        return input("What do you want the Architect to do?\n> ")
    else:
        path = "docs/final_prompt_to_architect.txt"
        if os.path.exists(path):
            with open(path) as f:
                return f.read().strip()
        return get_arg(1, "")
