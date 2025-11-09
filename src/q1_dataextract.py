import re
from pathlib import Path

def clean_title(t):
    # Remove isolated numbers
    t = re.sub(r'\b\d+\b', '', t)

    # Remove Roman numerals
    t = re.sub(r'\b[IVXLCM]+\b', '', t, flags=re.IGNORECASE)

    # Remove the word CONTENTS
    t = re.sub(r'\bCONTENTS\b', '', t, flags=re.IGNORECASE)

    # Keep letters, numbers, parentheses, hyphens, and spaces
    t = re.sub(r'[^A-Za-z0-9\-\(\) ]+', '', t)

    # Normalize spacing
    t = re.sub(r'\s+', ' ', t)

    return t.strip()


def populate_toc(tree):
    toc_pattern = re.compile(r'^(\d+(?:\.\d+)*)\s+(.+?)(?:\s+\d+)?$')

    try:
        current_path = Path(__file__).parent
    except NameError:
        current_path = Path.cwd()

    input_path = current_path / "Textbook.txt"
    if not input_path.exists():
        print(f"Error: Textbook.txt not found at {input_path}")
        return tree

    parsing_toc = False
    pending_path = None
    pending_title = ""

    lines = [line.strip() for line in input_path.open("r", encoding="UTF-8") if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("CONTENTS"):
            parsing_toc = True
            i += 1
            continue

        if parsing_toc and line.startswith("CHAPTER") and "INTRODUCTION" in line:
            break

        if not parsing_toc:
            i += 1
            continue

        m = toc_pattern.match(line)

        if m and line.lower().startswith("section"):
            m = None

        if m:
            if pending_path:
                tree.insert(pending_path, clean_title(pending_title))

            num_str = m.group(1)
            pending_path = num_str.split('.')

            if int(pending_path[0]) > 10:
                break

            pending_title = m.group(2).strip()

            while i + 1 < len(lines) and re.match(r'^[a-z]', lines[i + 1]):
                pending_title += " " + lines[i + 1]
                i += 1

        i += 1

    if pending_path:
        tree.insert(pending_path, clean_title(pending_title))

    return tree