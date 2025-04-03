from core.wrapper import with_reflection

@with_reflection
def parse_module_list(raw):
    modules = []
    for line in raw.split("\n"):
        if "-" in line and ":" in line:
            try:
                _, rest = line.split("-", 1)
                func, desc = rest.strip().split(":", 1)
                modules.append({
                    "filename": f"{func.strip()}.py",
                    "function": func.strip(),
                    "description": desc.strip()
                })
            except:
                continue
    return modules
