
def parse_python_file(file_path, base):
    with file_path.open("r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    summary = {
        "filename": str(file_path.relative_to(base)),
        "type": ".py",
        "functions": [],
        "description": ""
    }

    for line in lines:
        line = line.strip()
        if line.startswith("def "):
            fn = line.split("def ")[1].split("(")[0]
            summary["functions"].append(fn)
        elif line.lower().startswith("print(") or "description" in line.lower():
            summary["description"] = line.replace("print(", "").replace(")", "").strip("'"")

    return summary
