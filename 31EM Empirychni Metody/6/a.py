import itertools

def gc(obs):
    c=[]
    for r in range(1,len(obs)+1):
        c+=itertools.combinations(obs,r)
    return c

vs=['x1','x2','x3']
co=gc(vs)
print([c for c in co if len(c)==2])