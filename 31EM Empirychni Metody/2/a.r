v=19
n=v*100
m=v
s=v/10

d=rnorm(n,m,s)
d

cfile='E:\\Universytet\\31EM Empirychni Metody\\2\\a.xlsx'
tfile='E:\\Universytet\\31EM Empirychni Metody\\2\\a.txt'

library(openxlsx)
write.table(d,cfile)