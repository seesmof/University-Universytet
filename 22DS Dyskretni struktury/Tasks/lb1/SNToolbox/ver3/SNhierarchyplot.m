function SNhierarchyplot(SN, Plotprop)

% find hierarchy
h=SNhierarchy(SN);
mindxt=realmax;
% plot hierarchy

hlevels=max(h); 
%d(1:length(h),1:2)=0;
d=zeros(length(h),2);
dy=double(100./hlevels);
for ht=1:1:hlevels
    lvy=100-(ht.*dy)+0.5.*dy;
    r=find(h==ht);
    dxht=100./length(r); 
    dd(ht)=dxht*0.01;
    if dxht<mindxt
       mindxt=dxht;
    end;
    nel=1;
    for i=r
        d(i,1)=(nel-0.5).*dxht;
        d(i,2)=lvy;
        ws=SN.node{i};
        starr(i,1:length(ws))=ws;
        nel=nel+1;
    end;    
end;
d=d./100; 
ss=strcat('o',Plotprop.NodeColour);
hold on;
plot(d(:,1),d(:,2),ss);
x=1;
for i=1:1:length(h)
    if d(i,1)<0.5
       zu(i,1)=d(i,1)-0.25.*dd(h(i)); 
    else
       zu(i,1)=d(i,1)-0.1.*dd(h(i));
    end;
    if h(i)<hlevels
       zu(i,2)=d(i,2)+0.0015.*dy;
    else
       zu(i,2)=d(i,2)-0.0015.*dy.*x;
       x=-x;
    end;
end;
text(zu(:,1),zu(:,2),starr);
My_cell=cell(length(h));
x = strcmp(strtok(SN.relation),strtok(My_cell));
for i=1:1:length(h)
    for j=find(x(i,:)==0)
        %annotation('arrow',[d(i,1) d(j,1)],[d(i,2) d(j,2)],'Color', Plotprop.RelationColour);
        SNarrowtxt(d(i,1),d(i,2), d(j,1), d(j,2), SN.relation{i,j},Plotprop.RelationColour, [0 0.5 0.2]);
    end;
end;
