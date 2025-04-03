from core.template_header import *
from core.wrapper import wrap_execution
import re

@wrap_execution
def create_module(name):
    # Clean and shorten name
    clean = re.sub(r'[^\w\d_\- ]+', '', name).strip().replace(" ", "_")
    truncated = clean[:40].lower() or "module"
    filename = f"{truncated}.py"

    if os.path.exists(filename):
        print(f"[SKIP] Module {filename} already exists.")
        return

    with open(filename, "w") as f:
        f.write(f'print("Module {name} created.")\n')

    print(f"[REFLECT] Module {filename} created.")
