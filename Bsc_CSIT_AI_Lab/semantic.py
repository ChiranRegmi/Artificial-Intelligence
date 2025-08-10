#Semantic Analysis


import nltk
from nltk.corpus import wordnet

# Download WordNet data (only first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to get meanings/synonyms of a word
def get_semantics(word):
    synsets = wordnet.synsets(word)
    
    if not synsets:
        print(f"No meaning found for '{word}'")
        return

    print(f"\nMeanings of the word '{word}':")
    for i, syn in enumerate(synsets[:3], start=1):  # limit to first 3 meanings
        print(f"{i}. Definition: {syn.definition()}")
        print(f"   Synonyms: {[lemma.name() for lemma in syn.lemmas()]}")
        print()

# Example usage
word = input("Enter a word: ")
get_semantics(word)
