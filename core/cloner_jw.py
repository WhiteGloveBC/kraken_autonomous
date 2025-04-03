from core.template_header import *
from core.wrapper import wrap_execution
from core.template_footer import *
import shutil, os

@wrap_execution
def clone_module(base_name, count=3):
    for i in range(1, count + 1):
        src = f"core/{base_name}.py"
        dst = f"clones/{base_name}_jw{i}.py"
        if not os.path.exists("clones"):
            os.makedirs("clones")
        shutil.copy(src, dst)
        reflect(f"Clone created: {dst}")
    finalize()

if __name__ == "__main__":
    name = get_arg(1, "troubleshooter")
    count = int(get_arg(2, 3))
    clone_module(name, count)
