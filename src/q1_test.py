# 1. Import the classes and functions from your other files.
from q1_tree import TocTree
from q1_dataextract import populate_toc 

print("="*80)
print("Running Q1 Implementation...")
print("="*80)

# 2. Create the tree
book_title = "Machine Learning"
# CITATION: This TOC is from "Machine Learning" 
# by Tom M. Mitchell (McGraw-Hill, 1997), per 'Textbook.txt'.
my_toc = TocTree(book_title) 

# 3. Populate it with data
populate_toc(my_toc) 
print(f"Successfully populated the tree for '{book_title}'.\n")

# 4. Demonstrate print_toc (Mode: 'plain')
my_toc.print_toc(mode='plain')

# 5. Demonstrate print_toc (Mode: 'indented')
my_toc.print_toc(mode='indented')

# 6. Demonstrate print_toc (Mode: 'indented_num')
my_toc.print_toc(mode='indented_num')

# 7. Demonstrate height()
print("\n" + "-"*80)
print("Tree Height and Depth Demonstration")
print(f"Total Height of the tree (max depth): {my_toc.height()}")


# 8. Demonstrate depth(num_str, node_title)
print("\n--- Node Depths ---")
print(f"Depth of '4.5.1 A Differentiable Threshold Unit': {my_toc.depth('4.5.1', 'A Differentiable Threshold Unit')}")
print(f"Depth of '4.5 Multilayer Networks...': {my_toc.depth('4.5', 'Multilayer Networks and the BACKPROPAGATION Algorithm')}")
print(f"Depth of '4 Artificial Neural Networks': {my_toc.depth('4', 'Artificial Neural Networks')}")
print(f"Depth of '{book_title}' (Root): {my_toc.depth('0', book_title)}")
print(f"Depth of 'Non-existent Title': {my_toc.depth('99', 'Non-existent Title')}")
print("-"*80)