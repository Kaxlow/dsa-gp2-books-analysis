import pytest
import pandas as pd
from book_analysis import textpreprocessing, textanalysis

# Use first four lines of Pride and Prejudice text for tests
tokens = textpreprocessing.txt_preprocessing(txt_file = "PrideAndPrejudice_test.txt")

# Pytest

# Test txt_preprocessing function
def test_txt_preprocessing():
  
  # Verify that tokens is a list
  assert isinstance(tokens, list)

  # Verify the existence of certain expected tokens  
  expected_tokens = ["acknowledged", "possession", "however", "neighbourhood", "mr", "bennet", "netherfield", "replied", "feelings", "lady"]
  for token in expected_tokens:
    assert token in tokens

# Test TextAnalysis class and its methods
txt_analysis = textanalysis.TextAnalysis(tokens)

# Test lettercounter method
def test_lettercounter():
  result = txt_analysis.lettercounter(table = True, plot = False)
  # Verify that result is a DataFrame
  assert isinstance(result, pd.DataFrame)
  # Verify that the DataFrame has two columns for letter and count
  assert list(result.columns) == ['Letter', 'Count']
  # Verify that the counts are >= 0
  assert all(isinstance(count, int) and count >= 0 for count in result['Count'])

# Test wordcounter method
def test_wordcounter():
  result = txt_analysis.wordcounter(table = True, plot = False)
  # Verify that result is a DataFrame
  assert isinstance(result, pd.DataFrame)
  # Verify that the DataFrame has two columns for word and count
  assert list(result.columns) == ['Words', 'Count']
  # Verify that the counts are >= 0
  assert all(isinstance(count, int) and count >= 0 for count in result['Count'])

# Test kgramcounter method
def test_kgramcounter():
  for n in [2, 3]:
    result = txt_analysis.kgramcounter(k = n, plot = False)
    # Verify that result is a DataFrame
    assert isinstance(result, pd.DataFrame)
    # Verify that the DataFrame has two columns for k-gram and count
    assert list(result.columns) == ['K-gram', 'Count']
    # Verify that the counts are >= 0
    assert all(isinstance(count, int) and count >= 0 for count in result['Count'])