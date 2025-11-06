import textpreprocessing, textanalysis

# Run text preprocessing on Pride and Prejudice
txt = textpreprocessing.txt_preprocessing()

# Create an instance of TextAnalysis with the preprocessed text
txt_analysis = textanalysis.TextAnalysis(txt)

# Find frequencies of letters a-z
txt_analysis.lettercounter()

# Find the 40 most common words and their frequencies
txt_analysis.wordcounter()

# Find the 20 most common bigrams and their frequencies
txt_analysis.kgramcounter(k=2)

# Find the 20 most common trigrams and their frequencies
txt_analysis.kgramcounter(k=3)