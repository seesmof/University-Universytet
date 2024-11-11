TABLE_FILE_PATH='E:\\Universytet\\31EM Empirychni Metody\\2\\a.xlsx'

v=19
n=v*100
m=v
s=v/10

dataset=rnorm(n,m,s)
write.table(dataset,TABLE_FILE_PATH)

dataset.arr=array(dataset,dim=c(v,s))
dataset.arr

hist(dataset.arr,main='Histogram of observed data ALLELUJAH')
plot(density(dataset.arr),main='Density estimate of data ALLELUJAH')

probabilities.arr=pnorm(dataset.arr,mean=m,sd=s)
# this one is for Pearson
chisq.test(probabilities.arr)
# this one is for Kolmogorom
ks.test(dataset.arr,probabilities.arr)