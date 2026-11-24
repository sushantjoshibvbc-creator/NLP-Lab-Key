from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample dataset
texts = [
    "I love this product",
    "This is a great experience",
    "I am very happy",
    "I hate this product",
    "This is a bad experience",
    "I am very disappointed"
]

# Labels
labels = [
    "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative"
]

# Create Naive Bayes model
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# Train model
model.fit(texts, labels)

# Test new text
new_text = ["I love this experience"]

prediction = model.predict(new_text)

print("Input Text:", new_text[0])
print("Predicted Category:", prediction[0])