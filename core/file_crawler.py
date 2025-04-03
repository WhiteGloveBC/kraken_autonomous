from core.file_parser import parse_python_file
from core.file_creator import create_file
from pathlib import Path
import json

def crawl_python_files(root=".", output="core/file_index.json"):
    base = Path(root)
    summaries = []

    for file in base.rglob("*.py"):
        if file.is_file():
            summaries.append(parse_python_file(file, base))

    json_output = json.dumps(summaries, indent=2)
    create_file(str(base / output), json_output)
    print(f"[CRAWLER] Indexed {len(summaries)} .py files -> {output}")
