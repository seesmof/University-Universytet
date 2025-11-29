from nltk import load_parser
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'Який баланс у користувача admin'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)