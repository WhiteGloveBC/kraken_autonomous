from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import math

@wrap_execution
def escalate(current_count):
    new_count = math.ceil(current_count * 1.5)
    reflect(f"Escalating clone count from {current_count} to {new_count}")
    finalize()
    return new_count

if __name__ == "__main__":
    current = int(get_arg(1, 3))
    escalate(current)
