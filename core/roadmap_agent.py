from core.template_header import *
from core.wrapper import wrap_execution
from core.roadmap_storage import load_roadmap, save_roadmap
from core.roadmap_tools import add_to_roadmap, list_roadmap, dispatch_next

if __name__ == "__main__":
    arg = get_arg(1, None)
    if arg == "list":
        list_roadmap()
    elif arg == "dispatch":
        dispatch_next()
    elif arg:
        add_to_roadmap(" ".join(sys.argv[1:]))
    else:
        print("Usage:")
        print("  python roadmap_agent.py 'New roadmap entry'")
        print("  python roadmap_agent.py list")
        print("  python roadmap_agent.py dispatch")
