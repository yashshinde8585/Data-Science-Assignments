import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


with open('sample-para.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Tokenization (Word and Sentence)
words = word_tokenize(text)
sentences = sent_tokenize(text)

# Lowercasing
words = [word.lower() for word in words]

# Removing Punctuation
words = [word for word in words if word.isalpha()]

# Stopword Removal
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

# Frequency Distribution
fdist = FreqDist(lemmatized_words)

# Print Results
print(f"Original Text:\n{text[:500]}...")  # Display the first 500 characters
print(f"\nTokenized Words:\n{words[:20]}")
print(f"\nFiltered Words (No Stopwords, No Punctuation):\n{filtered_words[:20]}")
print(f"\nStemmed Words:\n{stemmed_words[:20]}")
print(f"\nLemmatized Words:\n{lemmatized_words[:20]}")
print(f"\nMost Common Words:\n{fdist.most_common(10)}")
