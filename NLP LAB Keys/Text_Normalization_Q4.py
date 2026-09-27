import re
text = "  NLP IS Amazing!!!   Python, is VERY useful.  "
print("Original Text:")
print(text)
text = text.lower( )
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()
print("\nNormalized Text:")
print(text)