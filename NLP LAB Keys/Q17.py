import spacy
import re
from collections import Counter

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Sample document
text = """
Google is a technology company founded by Larry Page
and Sergey Brin. It is headquartered in California.
The company develops software and internet services.
Google uses artificial intelligence in many products.
Its services are used by millions of people worldwide.
"""

# Process text
doc = nlp(text)

# Information Extraction
print("INFORMATION EXTRACTION")

for entity in doc.ents:
    print(entity.text, ":", entity.label_)

# Text Summarization
print("\nTEXT SUMMARIZATION")

# Calculate word frequency
words = [
    token.lemma_.lower()
    for token in doc
    if token.is_alpha and not token.is_stop
]

word_freq = Counter(words)

# Score each sentence
sentence_scores = {}

for sentence in doc.sents:
    score = sum(
        word_freq[token.lemma_.lower()]
        for token in sentence
        if token.is_alpha and not token.is_stop
    )

    sentence_scores[sentence] = score

# Select top 2 sentences
top_sentences = sorted(
    sentence_scores,
    key=sentence_scores.get,
    reverse=True
)[:2]

# Maintain original sentence order
summary = [
    sentence.text.strip()
    for sentence in doc.sents
    if sentence in top_sentences
]

print("Summary:")
print(" ".join(summary))

