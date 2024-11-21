import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Read the content of the text file
with open('sample-para.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text
tokens = word_tokenize(text)

# Compute word frequency distribution
fdist = FreqDist(tokens)

# Print the 10 most common words
print(fdist.most_common(10))
