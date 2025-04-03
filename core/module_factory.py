from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import os

@wrap_execution
def create_module(name):
    filename = f"{name}.py"
    if os.path.exists(filename):
        reflect(f"{filename} already exists.")
        return

    with open("core/module_template.py") as template:
        content = template.read().replace("{{MODULE_NAME}}", name)
    with open(filename, "w") as f:
        f.write(content)

    reflect(f"Module {filename} created.")
    finalize()

if __name__ == "__main__":
    module_name = get_arg(1, "new_module")
    create_module(module_name)
