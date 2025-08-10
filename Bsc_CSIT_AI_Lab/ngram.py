#Tokenization

import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Only needed once to download tokenizer models
nltk.download('punkt')

def generate_ngrams(text, n):
    words = word_tokenize(text.lower())  # Smarter tokenization
    return [tuple(words[i:i+n]) for i in range(len(words) - n + 1)]

def count_ngrams(text, n):
    ngrams = generate_ngrams(text, n)
    return Counter(ngrams)

# Example usage
text = "Hello, this is a simple example. Simple, isn't it?"
n = 2  # Bigram
ngram_counts = count_ngrams(text, n)

for ngram, count in ngram_counts.items():
    print(f"{ngram}: {count}")



   
