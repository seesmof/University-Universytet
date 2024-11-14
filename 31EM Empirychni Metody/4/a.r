n=19


o.vector=9:19
t.vector=7:17
cor(o.vector,t.vector)

g.vector=-3*o.vector+sample(1:19,1)
cor(o.vector,g.vector)


year=sample(2000:2024,n,replace=T)
rate=sample(1:10,n,replace=T)
plot(year,rate,main='Процентна ставка')

cor(year,rate)


o=sample(n,replace=T)
t=sample(n,replace=T)
o.matrix=matrix(o,nrow=n,ncol=n)
t.matrix=matrix(t,nrow=n,ncol=n)
o.matrix
t.matrix

x_csv="E:\\Universytet\\31EM Empirychni Metody\\4\\o.csv"
y_csv="E:\\Universytet\\31EM Empirychni Metody\\4\\t.csv"
write.csv(o.matrix, x_csv)
write.csv(t.matrix, y_csv)

print(cor.test(o.matrix,t.matrix,use='complete.obs'))