import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.template_header import *
from core.wrapper import wrap_execution

@wrap_execution
def push_changes(msg="ASZA commit"):
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", msg])
    run(["git", "push", "origin", "main"])
    reflect("Push complete")

if __name__ == "__main__":
    push_changes(get_arg(1, "ASZA commit"))
