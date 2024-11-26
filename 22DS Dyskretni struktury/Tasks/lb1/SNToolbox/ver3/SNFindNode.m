function SN2Fis(SN,d)
h=SN.nodetype;
% Searchng question nodes
quest=[];
for i=find(h==0)
    b=0;
    for j=find(h==1)
        if isstr(SN.relation{i,j})
            if b==0
                quest(length(quest)+1)=i;
                mf(length(quest),1)=j;
                b=1;
            else
                b=b+1;
                mf(length(quest),b)=j;
            end;
        end;
    end;
end;
% End searcing
% Searching output1
out=[];
for i=1:length(h)
    if isstr(SN.relation{d,i})
        out(length(out)+1)=i;
    end;
end;
for i=1:length(out)
    b=1;
    st=out(i);
    while b>0
        b=0;
        r=[];
        for j=1:length(st)
            if SN.nodetype(st(j))==0
                for k=1:length(h)
                    if isstr(SN.relation{k,st(j)})&(k~=d)
                        r(length(r)+1)=k;
                        b=b+1;
                    end;
                end;
            else
                r(length(r)+1)=st(j);
            end;
        end;
    st=r;
    end;
    outr=zeros(size(quest));
    outt=outr';
    for j=1:length(st)
        [k,k2]=find(st(j)==mf);
        outt(k,outr(k)+1)=st(j);
        outr(k)=outr(k)+1;
    end;    
end;
Fig=figure('DockControls','off','MenuBar','none','NumberTitle','off','Toolbar','none');
Txt=uicontrol('Style','text','Units','Normalized','Position',[0.3 0.9 0.4 0.05]);
BG=uibuttongroup('Units','normalized','Position',[0.3 0.3 0.4 0.5]);
for i=1:size(quest)
    set(Txt,'String',[SN.Node{quest(i)} '?']);
    
end;