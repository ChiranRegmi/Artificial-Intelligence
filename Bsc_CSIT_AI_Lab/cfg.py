#Context Free Grammer
import nltk
from nltk import CFG
# Download NLTK data (only needed once)
nltk.download('punkt')
# Define a simple context-free grammar (CFG)
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Det Adj N | 'I'
  VP -> V NP | V
  Det -> 'a' | 'the'
  N -> 'dog' | 'cat' | 'park'
  Adj -> 'big' | 'small'
  V -> 'saw' | 'walked'
""")
# Create a parser
parser = nltk.ChartParser(grammar)



I am a student in bmc.

# Input sentence
sentence = "I saw a big dog"
# Tokenize the sentence
tokens = nltk.word_tokenize(sentence)
# Parse the sentence
for tree in parser.parse(tokens):
    tree.pretty_print()
    tree.draw()  # Optional: Opens a tree diagram window
