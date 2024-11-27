from nltk import load_parser
p=load_parser('grammars/book_grammars/sql0.fcfg')
q='What cities are located in Greece'
t=list(p.parse(q.split()))
a=t[0].label()['SEM']
a=[s for s in a if s]
res=' '.join(a)
print(res)
from nltk.sem import chat80
nr=chat80.sql_query('corpora/city_database/city.db',res)
print(', '.join([w[0] for w in nr]))