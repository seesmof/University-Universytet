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