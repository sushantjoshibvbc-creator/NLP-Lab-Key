from collections import Counter
text = "Python is easy to learn. Python is powerful and easy."
words = text.lower().replace(".", "").split()
frequency = Counter(words)
print("Lexical Tokens: ") 
for word in words:
    print(word)
print("\nWord Frequency: ") 
for word, count in frequency.items():
    print(word, ":", count)