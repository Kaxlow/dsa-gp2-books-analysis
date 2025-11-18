class Node:
    """
    Attributes:
        title (str): The display title of the node (e.g., "Introduction").
        num_str (str): The numbering string (e.g., "1.2.1").
        parent (Node): A reference to the parent node.
        children (dict): A dictionary mapping sub-numbers to child Nodes.
    """
    def __init__(self, title, num_str=None, parent=None):
        self.title = title
        self.num_str = num_str
        self.parent = parent
        self.children = {}  

class TocTree:
    def __init__(self, book_title):
        """
        Initializes the tree with a root node.
        """
        self.root = Node(book_title, num_str="0")
        self.nodes_by_title = {(self.root.num_str, book_title): self.root}

    def insert(self, path, title):
        """
        Args:
            path (list[str]): The path
            title (str): The title
        """
        current = self.root
        
        for i, num in enumerate(path):
            is_last_num = (i == len(path) - 1)
            
            if num not in current.children:
                num_str = ".".join(path[:i+1])
                
                if is_last_num:
                    new_node = Node(title, num_str, parent=current)
                else:
                    new_node = Node(f"Section {num_str}", num_str, parent=current)
                
                current.children[num] = new_node
                
                unique_key = (new_node.num_str, new_node.title)
                self.nodes_by_title[unique_key] = new_node
                current = new_node
            
            else:
                current = current.children[num]
                if is_last_num and current.title != title:
                    old_unique_key = (current.num_str, current.title)
                    if "Section" in current.title:
                        self.nodes_by_title.pop(old_unique_key, None)
                    
                    current.title = title
                    current.num_str = ".".join(path)
                    
                    new_unique_key = (current.num_str, current.title)
                    self.nodes_by_title[new_unique_key] = current

    def print_toc(self, mode='indented_num'):
        """
        Args:
            mode (str): One of 'plain', 'indented', 'indented_num'.
        """
        print(f"\n--- Printing TOC: {self.root.title} (Mode: {mode}) ---")
        try:
            sorted_child_keys = sorted(self.root.children.keys(), key=int)
        except ValueError:
            sorted_child_keys = sorted(self.root.children.keys())
        
        for key in sorted_child_keys:
            self._print_recursive(self.root.children[key], mode)
        print("--- End of TOC ---")

    def _print_recursive(self, node, mode):

        number_str = node.num_str
        
        depth = number_str.count('.')
        indent = "  " * depth

        # Print based on mode
        if mode == 'plain':
            print(f"{node.title}")
        elif mode == 'indented':
            print(f"{indent}{node.title}")
        elif mode == 'indented_num':
            print(f"{indent}{number_str} {node.title}")
        else:
            if not hasattr(self, '_mode_error_printed'):
                print(f"Error: Unknown print mode '{mode}'")
                self._mode_error_printed = True
            print(f"{indent}{number_str} {node.title}")

        try:
            sorted_child_keys = sorted(node.children.keys(), key=int)
        except ValueError:
            sorted_child_keys = sorted(node.children.keys())
            
        for key in sorted_child_keys:
            self._print_recursive(node.children[key], mode)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node.children:
            if node.num_str == "0":
                return 0
            return len(node.num_str.split('.'))
    
        max_child_height = 0
        for child in node.children.values():
            max_child_height = max(max_child_height, self._height_recursive(child))
        
        return max_child_height

    def depth(self, num_str, node_title):
        unique_key = (num_str, node_title)
        node = self.nodes_by_title.get(unique_key)
        
        if not node:
            if node_title == self.root.title and num_str == "0":
                return 0
            return -1 
        
        depth = 0
        current = node
        while current.parent is not None:
            depth += 1
            current = current.parent
            
        return depth