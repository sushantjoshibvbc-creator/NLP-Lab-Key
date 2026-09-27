import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
text = "This is a simple example of natural language processing"
words = text.lower().split()
stop_words = set(stopwords.words('english'))
filtered_words = [ ]
for word in words:
    if word not in stop_words:
        filtered_words.append(word)
print("Original Text:")
print(text)
print("\n After Stop-word Removal: ")
print(filtered_words)