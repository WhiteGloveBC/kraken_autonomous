from core.template_header import *
from core.wrapper import wrap_execution

@wrap_execution
def get_arg(index, default=None):
    try:
        return sys.argv[index]
    except IndexError:
        return default

@wrap_execution
def parse_file_summary(path):
    if not os.path.exists(path):
        return None
    summary = {"filename": os.path.basename(path), "description": None}
    with open(path) as f:
        for line in f:
            if "print(" in line:
                summary["description"] = line.replace("print(", "").replace(")", "").strip(" '\"")
                break
    return summary
