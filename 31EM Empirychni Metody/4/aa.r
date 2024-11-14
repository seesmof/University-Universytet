v=19
n=v*100
m=v
s=v/10
data=rnorm(n,m,s)
d=matrix(data,nrow=n,ncol=m)

# third argument can be: everything OR all.obs OR complete.obs OR na.or.complete OR pairwise.complete.obs
cor(d,y=NULL,use='everything')
# can be: pearson OR spearman OR kendall
method=c('pearson','kendall','spearman')
