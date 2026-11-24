from textblob import TextBlob

# Customer reviews
reviews = [
    "The product is excellent",
    "I hate this service",
    "The product is average",
    "The experience was amazing",
    "The service is very poor"
]

# Sentiment Analysis
for review in reviews:

    analysis = TextBlob(review)
    score = analysis.sentiment.polarity

    if score > 0:
        sentiment = "Positive"

    elif score < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    print("Review:", review)
    print("Sentiment:", sentiment)
    print("Polarity Score:", score)
    print("----------------------")
