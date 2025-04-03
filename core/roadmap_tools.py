from core.wrapper import wrap_execution
from core.roadmap_storage import load_roadmap, save_roadmap
from core.pushover_alert import send_alert
from datetime import datetime

@wrap_execution
def add_to_roadmap(entry, source="manual"):
    roadmap = load_roadmap()
    item = {
        "id": len(roadmap) + 1,
        "entry": entry,
        "source": source,
        "timestamp": datetime.utcnow().isoformat()
    }
    roadmap.append(item)
    save_roadmap(roadmap)
    print(f"[ROADMAP] Added: {entry}")
    send_alert(f"Added to roadmap: {entry}", title="Roadmap")

@wrap_execution
def list_roadmap():
    roadmap = load_roadmap()
    if not roadmap:
        print("[ROADMAP] Empty.")
        return
    for item in roadmap:
        print(f"- {item['entry']} ({item['source']})")

@wrap_execution
def dispatch_next():
    roadmap = load_roadmap()
    if not roadmap:
        print("[ROADMAP] Nothing to dispatch.")
        return
    item = roadmap.pop(0)
    save_roadmap(roadmap)
    print(f"[ROADMAP] Dispatching: {item['entry']}")
    from core.architect_request import send_prompt_to_llm
    from core.architect_parser import parse_module_list
    from core.module_factory import create_module

    response = send_prompt_to_llm(item["entry"])
    if response:
        mods = parse_module_list(response)
        if mods:
            for m in mods:
                create_module(m)
