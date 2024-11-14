a='x1,x2,x3,x4,x12,x13,x14,x23,x24,x34'
a=[f'{e[:-1]}*x{e[-1:]}' if len(e)==3 else e for e in a.split(',')]
print(a)
