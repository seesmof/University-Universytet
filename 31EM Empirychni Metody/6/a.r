k=4
n=19

x1=sample(-1:1,n,T)
x2=sample(-1:1,n,T)
x3=sample(1:1,n,T)
x4=sample(-1:-1,n,T)

y=runif(n,17,19)

x12=x1*x2
x13=x1*x3
x14=x1*x4
x23=x2*x3
x24=x2*x4
x34=x3*x4

x=rbind(x1,x2,x3,x4,x12,x13,x14,x23,x24,x34)

a0=sum(y)/N
a=rep(0,10)

N=length(y)
M=length(a)

for (j in 1:N)
  for (k in 1:M)
    a[k]=a[k]+(y[j]*x[k,j])

for (k in 1:M)
  a[k]=a[k]/N

s=c('x1', 'x2', 'x3', 'x4', 'x1*x2', 'x1*x3', 'x1*x4', 'x2*x3', 'x2*x4', 'x3*x4')

s1=''
for (k in 1:M)
  s1=paste0(s1,sprintf('% + f*%s',a[k],s[k]))
s1