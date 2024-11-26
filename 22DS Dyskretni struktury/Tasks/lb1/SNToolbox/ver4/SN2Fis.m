function SN2Fis(SN,fname,SN_name)
fid=fopen(fname,'wb');
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
w=SNhierarchy(SN);
d=0;
for i=find(w==2)
    for j=find(w==max(w))
        if isstr(SN.relation{i,j})
            d=i;
        else
            break;
        end;
    end;
end;
%End searching output1
if d==0%d-node not found
    warndlg('Output not found','Error');
    return;
end;
out=[];
for i=1:length(h)
    if isstr(SN.relation{d,i})
        out(length(out)+1)=i;
    end;
end;
outx=zeros(0,length(quest)+1);
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
    for j=find(outr==0)
        outr(j)=1;
        outt(j,1)=0;
    end;
    W=My_fun(outt,outr);
    for j=1:size(W,1)
        outx(size(outx,1)+1,:)=[i W(j,:)];
    end;
end;
ch=[char(13) char(10)];
S=['[System]' ch 'Name=' char(39) SN_name char(39) ch 'Type=' char(39) 'mamdani' char(39) ch 'Version=2.0'...
    ch 'NumInputs=' num2str(length(quest)) ch 'NumOutputs=1' ch 'NumRules=' num2str(size(outx,2)) ch...
    'AndMethod=' char(39) 'min' char(39) ch 'OrMethod=' char(39) 'max' char(39) ch 'ImpMethod=' char(39) 'min' char(39) ...
    ch 'AggMethod=' char(39) 'max' char(39) ch 'DefuzzMethod=' char(39) 'centroid' char(39) ch ch];
for i=1:length(quest)
    S=[S '[Input' num2str(i) ']' ch 'Name=' char(39) SN.node{quest(i)} char(39) ch];
    l=find(mf(i,:)==0,1);
    if isempty(l)
        l=size(mf,2);
    else 
        l=l-1;
    end;
    S=[S 'Range=[ ]' ch 'NumMFs=' num2str(l) ch];
    for j=1:l
        S=[S 'MF' num2str(j) '=' char(39) SN.node{mf(i,j)} char(39) ':' char(39) 'trimf' char(39) ',[ ]' ch];
    end;
    S=[S ch];
end;
S=[S '[Output1]' ch 'Name=' char(39) SN.node{d} char(39) ch 'Range=[ ]' ch 'NumMFs=' num2str(length(out)) ch];
for i=1:length(out)
    S=[S 'MF' num2str(i) '=' char(39) SN.node{out(i)} char(39) ':' char(39) 'trimf' char(39) ',[ ]' ch];
end;
S=[S ch '[Rules]' ch];
for i=1:size(outx,1)
    for j=2:size(outx,2)
        S=[S num2str(outx(i,j)) ' '];
    end;
    S=[S(1:length(S)-1) ', ' num2str(outx(i,1)) ' (1) : 1' ch];
end;
fwrite(fid,S,'char');
fclose(fid);