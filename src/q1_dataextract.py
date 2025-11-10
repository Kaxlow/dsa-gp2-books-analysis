import re
from pathlib import Path

class TreeNode:
    def __init__(self, title):
        self.title = title
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class TOCTree:
    def __init__(self, root_title="Machine Learning"):
        self.root = TreeNode(root_title)

    def insert(self, numbering_list, title):
        current = self.root
        for num in numbering_list:
            idx = int(num) - 1
            while len(current.children) <= idx:
                current.children.append(TreeNode(None))
            if current.children[idx].title is None:
                current.children[idx].title = title
            current = current.children[idx]

    def print_plain(self):
        def dfs(node):
            if node.title:
                print(node.title)
            for child in node.children:
                dfs(child)
        dfs(self.root)

    def print_indented(self):
        def dfs(node, depth=0):
            if node.title:
                print("  " * depth + node.title)
            for child in node.children:
                dfs(child, depth + 1)
        dfs(self.root)

    def print_indented_numbered(self):
        def dfs(node, numbering):
            if node.title:
                print(f"{numbering} {node.title}".strip())
            for i, child in enumerate(node.children, 1):
                dfs(child, f"{numbering}.{i}" if numbering else f"{i}")
        dfs(self.root, "")

    def height(self):
        def get_height(node):
            if not node.children:
                return 0
            return 1 + max(get_height(child) for child in node.children)
        return get_height(self.root)

    def depth(self, num_str, title):
        target = (num_str.strip(), title.strip().lower())

        def dfs(node, numbering, d):
            if node.title:
                if numbering == target[0] and node.title.lower() == target[1]:
                    return d
            for i, child in enumerate(node.children, 1):
                child_num = f"{numbering}.{i}" if numbering else f"{i}"
                res = dfs(child, child_num, d + 1)
                if res != -1:
                    return res
            return -1

        return dfs(self.root, "", 0)


def clean_title(title):
    title = re.sub(r'^\d+(?:\.\d+)*\s+', '', title).strip()
    return title


def remove_section(title):
    return bool(re.match(r'(?i)^section\s+\d+(\.\d+)*$', title.strip()))


def create_toc(tree):
    toc_pattern = re.compile(r'^(\d+(?:\.\d+)*)\s+(.+?)(?:\s+\d+)?$')

    try:
        current_path = Path(__file__).parent
    except NameError:
        current_path = Path.cwd()

    input_path = current_path / "Textbook.txt"
    if not input_path.exists():
        print(f"Error: Textbook.txt not found at {input_path}")
        return tree

    parsing = False
    pending_num = None
    pending_title = ""

    lines = [line.strip() for line in input_path.open("r", encoding="utf-8") if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("CONTENTS"):
            parsing = True
            i += 1
            continue

        if parsing and line.startswith("CHAPTER") and "INTRODUCTION" in line:
            break

        if not parsing:
            i += 1
            continue

        m = toc_pattern.match(line)
        if m:
            num_str = m.group(1)
            title = clean_title(m.group(2)).strip()

            if remove_section(title):
                i += 1
                continue

            if int(num_str.split('.')[0]) > 10:
                break

            if pending_num:
                tree.insert(pending_num, pending_title)

            pending_num = num_str.split('.')
            pending_title = title

            while i + 1 < len(lines) and re.match(r'^[a-z]', lines[i + 1]):
                pending_title += " " + lines[i + 1]
                i += 1

        i += 1

    if pending_num:
        tree.insert(pending_num, pending_title)

    return tree