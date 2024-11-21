import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download necessary NLTK data
nltk.download('punkt')

# Read the content of the text file
with open('sample-para.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the words
words = word_tokenize(text)

# Common English suffixes
suffixes = ['ing', 'ed', 'ly', 's', 'es', 'ment', 'ness', 'tion', 'able', 'ible']

# Initialize the stemmer
stemmer = PorterStemmer()

# Prepare to store results
results = []
suffix_word_count = 0  # Initialize the suffix word count

# Process each word
for word in words:
    # Skip non-alphabetical words
    if not word.isalpha():
        continue
    
    # Lowercase the word
    lower_word = word.lower()
    
    # Check for suffixes
    for suffix in suffixes:
        if lower_word.endswith(suffix):
            root_word = stemmer.stem(lower_word)
            results.append((word, suffix, root_word))
            suffix_word_count += 1  # Increment count for each suffix match
            break  # Stop after the first matching suffix

# Print total count of words with suffixes
print(f"Total number of words with the specified suffixes: {suffix_word_count}")

# Print results
print(f"\n{'Original Word':<20}{'Suffix':<10}{'Root Word':<20}")
print("="*50)
for original, suffix, root in results:
    print(f"{original:<20}{suffix:<10}{root:<20}")


#limitization for finding root words