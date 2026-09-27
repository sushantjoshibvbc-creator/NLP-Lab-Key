words = ["playing", "played", "player", "happiness", "carefully"]
suffixes = ["ing", "ed", "er", "ness", "ly"]
for word in words:
    found = False

    for suffix in suffixes:
        if word.endswith(suffix):
            root  =  word[ : -len(suffix)]
            print("Word:", word)
            print("Root:", root)
            print("Suffix:", suffix)
            print( )
            found = True
            break

    if not found:
        print("Word:", word)
        print("Root: No suffix identified")
        print( )