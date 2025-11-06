from pathlib import Path
import re
import nltk

# Define text preprocessing function which takes a text file and returns a list of tokenized words
def txt_preprocessing(txt_file = "PrideAndPrejudice.txt"):

    # Read all the text from Pride and Prejudice into a str var
    current_path = Path(__file__)
    input_path = current_path.parent.parent.resolve() / txt_file
    with input_path.open(mode = "r", encoding = "UTF-8") as file:
      txt = file.read()

    # Convert all text to lowercase
    txt = txt.lower()

    # Remove punctuation, digits, and special characters. Keep apostrophes.
    txt = re.sub(r"[^a-z\s\']", "", txt)

    # Tokenize text into a list of words by separating on whitespace
    txt = txt.split()
    # Count number of tokens before removing stopwords
    tokens_bef = len(txt)

    # Remove stopwords
    from nltk.corpus import stopwords
    en_stopwords = stopwords.words("english")
    txt = [word for word in txt if word not in en_stopwords]
    # Count number of tokens after removing stopwords
    tokens_aft = len(txt)

    # Token count summary
    print(f"Before removing stopwords, there were {tokens_bef} tokens.\nAfter removing the stopwords, there were {tokens_aft} tokens.")

    return txt