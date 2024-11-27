from nltk.tokenize import word_tokenize
from nltk.util import bigrams
text="ІСУС ХРИСТОС ГОСПОДЬ БОГ ВСЕМОГУТНІЙ ВСЕВИШНІЙ ВСЕСИЛЬНИЙ АМІНЬ СЛАВА ГОСПОДУ ІСУСУ ХРИСТУ НАВІКИ ВІЧНІ АМІНЬ"
tokens=word_tokenize(text)
bigrams_list=list(bigrams(tokens))
for b in bigrams_list:
    print(b)