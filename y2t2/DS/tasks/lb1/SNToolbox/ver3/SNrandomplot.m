function SNrandomplot(SN, Plotprop)
Nnodes=length(SN.node);
for i=1:1:Nnodes
    xx(i)=rand;
    yy(i)=rand;
end;
ss=strcat('o',Plotprop.NodeColour);
axes('position',[0 0 1 1]);
plot(xx,yy,ss); hold on;
v=axis; xleft=v(1); xrigth=v(2); ytop=v(4); ydown=v(3); dx=xrigth-xleft;dy=ytop-ydown;
xn=(xx-xleft)./dx; yn=(yy-ydown)./dy;
v(1)=xleft-0.1.*dx; v(2)=xrigth+0.1.*dx; v(3)=ydown-0.1.*dy; v(4)=ytop+0.1.*dy;
axis(v);
v=axis; xleft=v(1); xrigth=v(2); ytop=v(4); ydown=v(3); dx=xrigth-xleft;dy=ytop-ydown;
xn=(xx-xleft)./dx; yn=(yy-ydown)./dy;
for i=1:1:Nnodes
    if xn(i)<0.5
       text(xx(i)-0.08.*dx,yy(i),SN.node{i});
    else
       text(xx(i)+0.01.*dx,yy(i),SN.node{i});
    end;
end;
for i=1:1:Nnodes
    for j=1:1:Nnodes
        if isstr(SN.relation{i,j})
           %annotation('textarrow',[xn(i) xn(j)],[yn(i) yn(j)],'Color', Plotprop.RelationColour);
           SNarrowtxt(xx(i),yy(i), xx(j), yy(j), SN.relation{i,j},Plotprop.RelationColour, [0 0.5 0.2]);
        end;
    end;
end;
