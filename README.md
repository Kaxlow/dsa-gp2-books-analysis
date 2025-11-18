# Book Analysis

CU Boulder DTSC 5501-801 Group Project #2 - Data Structures in Action Table of Contents & Text Analysis

# Roles & Responsibilities

Written and maintained by Group 10:

* **[Ken Low]:** - Q2 text preprocessing, time and space complexity analysis, interpretation of letter, word, bigrams, and trigram distributions.
* **[Griffin Keener]:** - Q2 text analysis code that returns letter, word, bigram, and trigram frequencies, and sentence analysis code that shows sentence-structure metrics.
* **[Swejal Gabhane]:** - Q1 Data Parsing, Main script for testing, Report writeup
* **[Augustine Joy]:** - Q1 Tree data structure implementation, Packaging, README.md setup instructions.

# Setup and Execution

## Q1 Build a Table of Contents

This program parses the Table of Contents from `Textbook.txt`, builds a tree, and then prints the tree in multiple formats, along with its height and the depth of specific nodes.

### Prerequisites

All required modules (`re`, `pathlib`) are part of the standard Python library, so no `pip install` is necessary.

### File Structure

* `q1_tree.py`: Contains the `Node` and `TocTree` class definitions.
* `q1_dataextract.py`: Contains the `create_toc` function to parse the textbook.
* `q1_test.py`: The main script to test the program.
* `Textbook.txt`: The data file to be parsed.

### How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you have placed the four files.
3.  Execute the `q1_test.py` driver script using `python3`.

### Expected Output

When you run the script, the output will appear in this order:

1.  The complete Table of Contents printed in **'plain'** mode.
2.  The complete Table of Contents printed in **'indented'** mode.
3.  The complete Table of Contents printed in **'indented_num'** mode.
4.  A "Tree Height and Depth Demonstration" section, which prints the calculated height of the tree.
5.  A "Node Depths" section, which shows the results of the `depth()` function calls for the specific nodes being tested.

## Q2 Letters and Words Analysis

The code is configured to analyze the book "Pride and Prejudice". To execute the code and view the results of the book analysis, run the `FinalReport.ipynb` file.

The source code is located in `src/book_analysis`. It consists of the text preprocessing function in `textpreprocessing.py` and the text analysis class and methods in `textanalysis.py`.

The test script is available at `test/txtanalysis_test.py`.
