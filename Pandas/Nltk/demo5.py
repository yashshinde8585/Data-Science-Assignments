import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk import word_tokenize, pos_tag, FreqDist, sent_tokenize

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Read the text file
file_path = 'sample-para.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenize the text into words and sentences
words = word_tokenize(text)
sentences = sent_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(words)

# Initialize counters
word_count = len(words)
sentence_count = len(sentences)
verb_count = sum(1 for word, tag in pos_tags if tag.startswith('VB'))
noun_count = sum(1 for word, tag in pos_tags if tag.startswith('NN'))
adjective_count = sum(1 for word, tag in pos_tags if tag.startswith('JJ'))

# Calculate frequency distribution of words
freq_dist = FreqDist(words)

# Print the results
print(f"Total words: {word_count}")
print(f"Total sentences: {sentence_count}")
print(f"Total verbs: {verb_count}")
print(f"Total nouns: {noun_count}")
print(f"Total adjectives: {adjective_count}")
print("\nWord Frequency (Top 10):")
for word, freq in freq_dist.most_common(828):
    print(f"{word}: {freq}")