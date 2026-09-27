import nltk
nltk.download('punkt')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('averaged_perceptron_tagger_eng')
from nltk import word_tokenize, pos_tag, ne_chunk
text = "Alex works at BVBC in Delhi."
words = word_tokenize(text)
tags = pos_tag(words)
entities = ne_chunk(tags)
print(entities)