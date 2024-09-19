v<-19
n<-v*10
m<-v
s<-v/10
gen<-rnorm(n,m,s)
hist(gen,col="green")
freq=table(gen)
gen.mean<-mean(gen)
med<-median(gen)
mode<-function(x) {
  ux<-unique(x)
  ux[which.max(tabulate(match(x,ux)))]
}
gen.mode<-mode(gen)
qua<-quantile(gen)

