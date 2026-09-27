import nltk
grammar = nltk.CFG.fromstring("""
S  -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'student' | 'book'
V -> 'reads'
""")
parser = nltk.ChartParser(grammar)
sentence = "the student reads the book".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print( )