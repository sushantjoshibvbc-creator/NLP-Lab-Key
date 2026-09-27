import nltk
grammar = nltk.CFG.fromstring("""
S     -> NP VP
NP  -> Det N
VP  -> V NP
Det  -> 'the' | 'a'
N    -> 'boy' | 'girl' | 'ball'
V   -> 'kicks' | 'throws'
""")
parser = nltk.ChartParser(grammar)
sentence = "the boy kicks a ball".split()
print("Parse Tree:")
for tree in parser.parse(sentence):
    print(tree)