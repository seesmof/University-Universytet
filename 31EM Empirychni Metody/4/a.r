x.vector=9:19
y.vector=7:17
cor(x.vector,y.vector)

z.vector=-3*x.vector+8
cor(x.vector,z.vector)

n=7
year=sample(2000:2024,n,replace=T)
sort(year)
rate=sample(1:10,n,replace=T)
sort(rate)
plot(year,rate,main='Процентна ставка')
