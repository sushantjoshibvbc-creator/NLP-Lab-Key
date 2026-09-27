import nltk

nltk.download('wordnet')
nltk.download('punkt_tab')

from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence1 = "I went to the bank to deposit money."
sentence2 = "The fisherman sat on the bank of the river."

words1 = word_tokenize(sentence1)
words2 = word_tokenize(sentence2)

sense1 = lesk(words1, 'bank')
sense2 = lesk(words2, 'bank')

print("Sentence 1:")
print(sentence1)
print("Meaning:", sense1.definition())

print("\nSentence 2:")
print(sentence2)
print("Meaning:", sense2.definition())