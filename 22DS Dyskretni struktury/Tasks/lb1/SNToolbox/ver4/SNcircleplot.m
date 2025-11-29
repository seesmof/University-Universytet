function SNcircleplot(SN, Plotprop)
Nnodes=length(SN.node);
dalfa=(2.*pi)./Nnodes;
for i=1:1:Nnodes
    alfa=(i-1).*dalfa;
    xx(i)=Plotprop.CircleRadius.*cos(alfa);
    yy(i)=Plotprop.CircleRadius.*sin(alfa);
end;
ss=strcat('o',Plotprop.NodeColour);
axes('position',[0 0 1 1]);
plot(xx,yy,ss);
hold on;
v=axis; xleft=v(1); xrigth=v(2); ytop=v(4); ydown=v(3); dx=xrigth-xleft;dy=ytop-ydown;
xn=(xx-xleft)./dx; yn=(yy-ydown)./dy;
v(1)=xleft-0.1.*dx; v(2)=xrigth+0.1.*dx; v(3)=ydown-0.1.*dy; v(4)=ytop+0.1.*dy;
axis(v);
v=axis; xleft=v(1); xrigth=v(2); ytop=v(4); ydown=v(3); dx=xrigth-xleft;dy=ytop-ydown;
xn=(xx-xleft)./dx; yn=(yy-ydown)./dy;
for i=1:1:Nnodes
    alfa=(i-1).*dalfa;
    if and(alfa>0.5.*pi, alfa<1.5.*pi)
       text(xx(i)-0.09.*dx,yy(i),SN.node{i});
    else
       text(xx(i)+0.01.*dx,yy(i),SN.node{i});
    end;
end;
My_cell=cell(Nnodes);
x = strcmp(strtok(SN.relation),strtok(My_cell));
for i=1:1:Nnodes
    for j=find(x(i,:)==0)
        %annotation('textarrow',[xn(i) xn(j)],[yn(i) yn(j)],'Color',Plotprop.RelationColour);
        SNarrowtxt(xx(i),yy(i), xx(j), yy(j), SN.relation{i,j},Plotprop.RelationColour, [0 0.5 0.2]);
    end;
end;
