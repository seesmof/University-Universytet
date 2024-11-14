import itertools

def gc(obs):
    c=[]
    for r in range(1,len(obs)+1):
        c+=itertools.combinations(obs,r)
    return c

# do this manually JESUS plEASE HELp
vs=['x1','x2','x3','x4']
co=gc(vs)
print([c for c in co if len(c)==2])

'''
x12
x13
x14
x23
x24
x34
'''