from pathlib import Path
from core.reality_check import reality_check

reality_check()

def run():
    context_path = Path("context/context.md")
    output_path = Path("docs/index.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not context_path.exists():
        print("Context file not found.")
        return

    content = context_path.read_text()

    header = "# ASZA Documentation\n\n"
    intro = "This documentation is automatically generated from the system context.\n\n"
    output = header + intro + content

    output_path.write_text(output)
    print(f"Documentation written to {output_path}")

if __name__ == "__main__":
    run()
