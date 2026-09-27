import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ["playing", "played", "plays", "studies",
               "studying", "happiness", "connected"]
print("Word\t\t Stem")
for word in words:
    print(word, "\t\t", stemmer.stem(word))