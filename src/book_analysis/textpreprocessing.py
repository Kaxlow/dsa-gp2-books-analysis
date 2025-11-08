import re
import nltk

def txt_preprocessing(txt_file = "data/PrideAndPrejudice.txt"):

  '''
  This function takes a .txt file and returns a list of tokenized words by performing the following steps:
  1. Read the contents of a .txt file into a string variable. By defaults, it reads the text from the book "Pride and Prejudice".
  2. Converts all letters into lowercase.
  3. Removes all punctuation, digits, and special characters, while keeping apostrophes.
  4. Tokenizes the text into a ist of words by separating on whitespace.
  5. Removes common English stopwords from the list of tokens, using ntlk.corpus's stopwords list as reference.

  The function also prints a summary showing the number of tokens before and after removing the stopwords.
  '''

  # Read text from .txt file into a string
  with open(txt_file, mode = "r", encoding = "UTF-8") as file:
    txt = file.read()

  # Convert all text to lowercase
  txt = txt.lower()

  # Remove punctuation, digits, and special characters. Keep apostrophes.
  txt = re.sub(r"[^a-z\s\']", "", txt)

  # Tokenize text into a list of words by separating on whitespace
  txt = txt.split()
  # Count number of tokens before removing stopwords
  tokens_bef = len(txt)

  # Remove stopwords from list of tokens
  from nltk.corpus import stopwords
  en_stopwords = stopwords.words("english")
  txt = [word for word in txt if word not in en_stopwords]
  # Count number of tokens after removing stopwords
  tokens_aft = len(txt)

  # Token count summary
  print(f"Before removing stopwords, there were {tokens_bef} tokens.\nAfter removing the stopwords, there were {tokens_aft} tokens.")

  return txt