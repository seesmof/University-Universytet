function h=SNhierarchy(SN)
% find hierarchy
Nnodes=length(SN.node); nl=SN.node;
h(1:Nnodes)=intmax; hh=1; 
while and(length(nl)>0, hh<=Nnodes)
    N1=length(nl); ht=h; nlt=nl;
    for k=1:1:N1
        j=isnodepresent(SN.node, nl{k});
        flag=0;
           for i=1:1:Nnodes
               if and(h(i)>hh,i~=j)
                  if isstr(SN.relation{i,j})==1
                     flag=flag+1;
                  end;
               end;
           end;
           if flag==0
              jt=isnodepresent(nlt, nl{k});
              ht(j)=hh; nlt{jt}=[];
           end;
    end;
    h=ht; ht=[]; hh=hh+1;  z=1; nl=[];
    for i=1:1:length(nlt)
        if isstr(nlt{i})==1
           nl{z}=nlt{i}; z=z+1;
        end;
    end;
    nlt=[];
end; % while

function kk=isnodepresent(SS, NN)
% if node is present return it's position, otherwise return 0.
kk=0;
for ii=1:1:length(SS)
    if strcmp(SS{ii}, NN)==1
       kk=ii;
       break;
    end;
end;

