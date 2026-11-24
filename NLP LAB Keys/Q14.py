from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Sample text documents
documents = [
    "Python is easy to learn",
    "Python is useful for data analytics",
    "Data analytics is interesting"
]

# Bag of Words
bow = CountVectorizer()
bow_matrix = bow.fit_transform(documents)

print("Bag of Words:")
print(bow.get_feature_names_out())
print(bow_matrix.toarray())

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

print("\nTF-IDF:")
print(tfidf.get_feature_names_out())
print(tfidf_matrix.toarray( ))