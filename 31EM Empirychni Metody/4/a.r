v=19
n=v*100
m=v
s=v/10
data=rnorm(n,m,s)
d=matrix(data,nrow=n,ncol=m)

cor(d,y=NULL,use='everything')
method=c('pearson','kendall','spearman')
