from q1_tree import TocTree
from q1_dataextract import create_toc

book_title = "Machine Learning"
my_toc = TocTree(book_title)

create_toc(my_toc)

# Display: 'plain'
my_toc.print_toc(mode='plain')

# Display: 'indented'
my_toc.print_toc(mode='indented')

# Display: 'indented_num'
my_toc.print_toc(mode='indented_num')

print("\n" + "-"*80)
print("Tree Height and Depth Demonstration")
print(f"Total Height of the tree (max depth): {my_toc.height()}")
print("\n" + "-"*80)

print("\n" + "-"*80)
print("\n--- Node Depths ---")
print(f"Depth of 4.5.1 A Differentiable Threshold Unit': {my_toc.depth('4.5.1', 'A Differentiable Threshold Unit')}")
print(f"Depth of 3.7 Issues in Decision Tree Learning': {my_toc.depth('3.7', 'Issues in Decision Tree Learning')}")
print(f"Depth of 4 Artificial Neural Networks': {my_toc.depth('4', 'Artificial Neural Networks')}")
print(f"Depth of {book_title}' (Root): {my_toc.depth('0', book_title)}")
print(f"Depth of 'Non-existent Title': {my_toc.depth('10', 'Title')}")
print("-"*80)