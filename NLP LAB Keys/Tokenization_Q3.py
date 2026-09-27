import re

text = "Natural Language Processing is interesting. Python makes NLP easy."

# Sentence Tokenization
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

print("Sentence Tokenization:")
for sentence in sentences:
    print(sentence)

# Word Tokenization
words = re.findall(r'\b\w+\b|[.!?]', text)

print("\nWord Tokenization:")
print(words)
