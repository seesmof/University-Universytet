x.vector=9:19
y.vector=7:17
cor(x.vector,y.vector)

z.vector=-3*x.vector+8
cor(x.vector,z.vector)

n=7
year=sample(2000:2024,n,replace=T)
rate=sample(1:10,n,replace=T)
plot(year,rate,main='Процентна ставка')

cor(year,rate)


n=19
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