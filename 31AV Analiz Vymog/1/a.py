import random as r
import string as s

n=12
res=r.choices(s.ascii_lowercase+s.digits,k=n)
print(''.join(res))