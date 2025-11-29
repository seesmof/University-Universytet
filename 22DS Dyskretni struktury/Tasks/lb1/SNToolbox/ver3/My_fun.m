function [V]=My_fun(A,n);
l=ones(length(n),1);
for i=length(n)-1:-1:1
    l(i)=l(i+1)*n(i+1);
end;
for i=0:l(1)*n(1)-1
    e=i;
    for j=1:length(n)
        q=fix(e/l(j));
        V(i+1,j)=A(j,q+1);
        e=e-q*l(j);
    end;
end;