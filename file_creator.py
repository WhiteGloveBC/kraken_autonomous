import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "core")))

from template_header import *
from wrapper import wrap_execution
from template_footer import *

@wrap_execution
def create_file(filename):
    if os.path.exists(filename):
        reflect(f"{filename} already exists.")
        return

    with open("core/module_template.py") as template:
        content = template.read().replace("{{MODULE_NAME}}", filename.replace(".py", ""))
    with open(filename, "w") as f:
        f.write(content)

    reflect(f"{filename} created.")
    finalize()

if __name__ == "__main__":
    name = get_arg(1, "new_file.py")
    create_file(name)
