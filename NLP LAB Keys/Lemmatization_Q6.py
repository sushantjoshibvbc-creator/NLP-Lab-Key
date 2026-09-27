words = ["dogs", "cars", "playing", "played", "studies"]

def lemmatize(word):
    if word.endswith("ies"):
        return word[:-3] + "y"
    elif word.endswith("ing"):
        return word[:-3]
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("s"):
        return word[:-1]
    else:
        return word

print("Word\t\tLemma")

for word in words:
    print(word, "\t\t", lemmatize(word))