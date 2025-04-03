from core.template_header import *
from core.wrapper import wrap_execution
from core.file_parser import get_arg

@wrap_execution
def get_prompt(interactive=True):
    if interactive:
        return input("What do you want the Architect to do?\n> ")
    else:
        return get_arg(1, None)
