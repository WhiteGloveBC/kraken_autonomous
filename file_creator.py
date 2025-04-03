def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"[FILE CREATED] {path}")
