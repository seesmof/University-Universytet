function SN2E2Go(SN,fname)
fid=fopen(fname,'wb');
h=SN.nodetype;
% Searchng question nodes
quest=[];
for i=find(h==0)
    for j=find(h==1)
        if isstr(SN.relation{i,j})
            quest(length(quest)+1)=i;
            break;
        end;
    end;
end;
% End searcing
% Searching d-node
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
%End searching d-node
if d==0%d-node not found
    warndlg('Node not found','Error');
    return;
end;
h(d)=1;
k=1;
%RULEs
while k>0
    k=0;
    q=[];
    for i=find(h==0)
        for j=1:length(h)
            if isstr(SN.relation{j,i})
                if h(j)==1
                    q(length(q)+1)=j;
                else
                    q=[];
                    break;
                end;
            end;
        end;
        if ~isempty(q)
            S=['RULE [' char(SN.node{i}) ']' char(13) char(10)];
            fwrite(fid,S,'char');
            S='If ';
            % nodes with questions searching
            for j=quest
                zzz=[];
                for l=q
                    if isstr(SN.relation{j,l})
                        zzz(length(zzz)+1)=l;
                    end;
                end;
                if ~isempty(zzz)                   
                    if length(zzz)==1
                        S=[S '[' char(SN.node{j}) '] =' ' "' char(SN.node{zzz(1)}) '" and' char(13) char(10)];
                    else
                        S=[S '[' char(SN.node{j}) '] : '];
                        for l=zzz
                            S=[S '"' char(SN.node{l}) '" '];
                        end;
                        S=[S  'and' char(13) char(10)];
                    end;
                    for l=zzz
                        for a=find(q==l)
                            q(a)=[];
                        end;
                    end;
                end;
            end;
            % end nodes with questions searching
            for j=1:max(w)
                zzz=[];
                for l=q
                    if (w(l)==j)&(SN.nodetype(l)==0)&(l~=d)
                        zzz(length(zzz)+1)=l;
                    end;
                end;
                if ~isempty(zzz)
                    if length(zzz)==1
                        S=[S '[MSL' num2str(j) '] =' ' "' char(SN.node{zzz(1)}) '" and' char(13) char(10)];
                    else
                        S=[S '[MSL' num2str(j) '] : '];
                        for l=zzz
                            S=[S '"' char(SN.node{l}) '" '];
                        end;
                        S=[S  'and' char(13) char(10)];
                    end;
                    for l=zzz
                        for a=find(q==l)
                            q(a)=[];
                        end;
                    end;
                end;
            end;
            S=[S(1:length(S)-6) char(13) char(10)];
            fwrite(fid,S,'char');
            if isempty(q)
                S=['Then [MSL' num2str(w(i)) '] = "' SN.node{i} '"' char(13) char(10)];
            else
                S=['Then [' SN.node{d} '] = "' SN.node{i} '"' char(13) char(10)];
            end;
            fwrite(fid,S,'char');
            h(i)=1;
            k=k+1;
        end;
    end;
end;
%End RULEs
%PROMPT
for i=quest
    S=['PROMPT [' SN.node{i} '] MultChoice' char(13) char(10) '"' SN.node{i} '?"' char(13) char(10)];
    for j=find(SN.nodetype==1)
        if isstr(SN.relation{i,j})
            S=[S '"' SN.node{j} '"' char(13) char(10)];
        end;
    end;
    fwrite(fid,S,'char');
end;
%End PROMPT
S=['GOAL [' SN.node{d} ']'];
fwrite(fid,S,'char');
fclose(fid);