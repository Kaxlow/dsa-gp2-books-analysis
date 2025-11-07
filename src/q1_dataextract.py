import re
from pathlib import Path # Used to handle file paths

def populate_toc(tree):
    # Regex to capture number, title, and optional page number at end of line
    # Groups: (1: number), (2: title)
    # This regex matches the number, then greedily matches the title (.*),
    # then optionally matches a space and a page number at the end (\s+\d+)?$
    toc_pattern = re.compile(r'^([\d\.]+)\s+(.*?)(\s+\d+)?$')

    # Regex for a line that is ONLY a title (continuation) or page number
    # This will match lines that DO NOT start with a number.
    title_only_pattern = re.compile(r'^(?![\d\.]+\s)(.*?)(\s+\d+)?$')

    try:
        current_path = Path(__file__).parent
    except NameError:
        current_path = Path.cwd()
        
    input_path = current_path / "Textbook.txt"

    if not input_path.exists():
        print(f"Error: Textbook.txt not found at {input_path}")
        print("Please make sure 'Textbook.txt' is in the same directory.")
        return tree

    parsing_toc = False
    pending_path = None
    pending_title = ""
    
    with input_path.open(mode="r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip()
            if not line: 
                continue

            if line.startswith("CONTENTS"):
                parsing_toc = True
                continue
            
            if line.startswith("CHAPTER") and "INTRODUCTION" in line:
                parsing_toc = False
                break
            
            if not parsing_toc:
                continue

            num_title_match = toc_pattern.match(line)
            title_only_match = title_only_pattern.match(line)

            if num_title_match:
                if pending_path:
                    tree.insert(pending_path, pending_title.strip())
                
                num_str = num_title_match.group(1)
                title = num_title_match.group(2).strip()
                path = num_str.split('.')
                
                if int(path[0]) > 10:
                    break
                    
                pending_path = path
                pending_title = title
            
            elif pending_path and title_only_match:
                title_continuation = title_only_match.group(1).strip()
                if title_continuation:
                    pending_title += f" {title_continuation}"

        if pending_path:
            tree.insert(pending_path, pending_title.strip())
    
    return tree 