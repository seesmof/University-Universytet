import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize

text='Some random text hopefully this will work LORD JESUS please help me FATHER GOD in JESUS HOLY NAME AMEN.'
tokens=word_tokenize(text)
pos_tags=nltk.pos_tag(tokens)
chunk_patterns=r'''
    NP: {<DT>?<JJ>*<NN>}
    VP: {<VB.*><NP|PP>}
'''
chunk_parser=RegexpParser(chunk_patterns)
res=chunk_parser.parse(pos_tags)
print(res)