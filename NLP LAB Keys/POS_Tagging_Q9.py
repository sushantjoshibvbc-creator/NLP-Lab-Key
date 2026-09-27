import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "The student is studying Python."

words = word_tokenize(text)

tags = pos_tag(words)

print("Word\tPOS Tag")

for word, tag in tags:
    print(word, "\t", tag)