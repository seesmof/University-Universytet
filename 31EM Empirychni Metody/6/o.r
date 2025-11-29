n=3
n

x1=seq(-1,1,by=0.1)
x2=seq(-1,1,by=0.01)
x3=seq(1,1,by=0.1)

y=seq(19,17,by=-0.1)

x12=x1*x2
x13=x1*x3
x23=x2*x3

x=rbind(x1,x2,x3,x12,x13,x23)
N=length(y)
a0=sum(y)/N
a=c(0,0,0,0,0,0)
M=length(a)
for (j in 1:N)
  for (i in 1:M)
    a[i]=a[i]+(y[j]*x[i,j])
for (i in 1:M)
  a[i]=a[i]/N
s=c('x1','x2','x3','x1*x2','x1*x3','x2*x3')
s1=''
for (i in 1:M)
  s1=paste0(s1,sprintf('%+f*%s',a[i],s[i]))
s2=paste0('y=',a0,s1)
s2

