function Res=SNfind(SN, SN1)
% Function Res=SNfind(SN, SN1) find the node of SN1 semantic
% network in SN semantic network. The goal node in SN1 must
% have name '?'. The Res value is [] if goal node is not 
% finded or node name if goal node is finded.
% The S1 must be a subnetwork of S.
% ----------------------------------------------------------
% (C)(R) 2005 by S.A. Subbotin - http://www.uanis.nm.ru

% data cheking
flag=0;
if isnodepresent(SN.node,'?')
   disp('Warning: The first argument contains a node [?]');
end;
if length(SN.node)>=length(SN1.node)
   nex(1:length(SN.node))=0;
   for i=1:1:length(SN1.node)
       if SN1.node{i}~='?'
          k=isnodepresent(SN.node, SN1.node{i});
          if k>0
             if SN.nodetype(k)==SN1.nodetype(i)
                nex(k)=1;
             else
                disp('Error: The first argument node [',S.node{k},'] and the second argument node [',S1.node{i},'] are nodes of different type');
                k=0;
             end;
          end;
       else
          k=1;
       end;
       if k==0
             disp('Error: The node [',SN1.node{i},'] is not exists in first argument semsntic network');
          flag==1;
       end;
   end;
else
   flag=1;
end;

% propagation

if  flag==0
    h=SNhierarchy(SN);

    if max(h)<intmax
        for ht=2:1:max(h)
            for i=1:1:length(h)
               if h(i)==ht
                  if nex(i)==0
                     nnn=0;iii=0;
                     for j=1:1:length(h)
                         if h(j)<ht
                            if isstr(SN.relation{j,i})==1
                               nnn=nnn+1;
                               if nex(j)==1
                                  iii=iii+1;
                               end;
                            end;
                         end;
                     end;
                     if SN.nodetype(i)==0 % AND node
                        if iii==nnn
                           nex(i)=1;
                        end;
                     else % OR node
                        if nnn>1
                           if iii==nnn
                              nex(i)=1;
                           end;
                        end;
                     end;
                  end; % if nex
               end; % if h(i)
            end; % for i
        end;% for ht

        % solution select

        goalind=isnodepresent(SN1.node,'?'); hi=[];li=[];
        for i=1:1:length(SN1.node)
            if isstr(SN1.relation{i,goalind})==1
               hi(length(hi)+1)=isnodepresent(SN.node, SN1.node{i});
            end;
            if isstr(SN1.relation{goalind,i})==1 
               li(length(li)+1)=isnodepresent(SN.node, SN1.node{i});
            end;
        end;
        Rh=[];
        for i=1:1:length(h)
            pr=0;po=0;
            for j=1:1:length(hi)
                if isstr(SN.relation{hi(j),i})==1
                   pr=pr+1;
                end;  
            end;
            for j=1:1:length(li)
                if isstr(SN.relation{i,li(j)})==1
                   po=po+1;
                end;  
            end;
            if and(and(pr==length(hi), po==length(li)), nex(i)==1)
               Rh(length(Rh)+1)=i;
            end;
        end;
        % forming a result 
        if length(Rh)==0
           Res=[];
           disp('RESULT: Goal node is not found')
        else
           disp(sprintf('RESULT: The number of founded solutions is %d',length(Rh)));
           for i=1:1:length(Rh)
               Res{i}=SN.node{Rh(i)};
           end;  
        end;
    else
       disp('Error: This function can not be be used for full connected networks');
    end;
else
    disp('Error: The second argument must be a subnetwork of first argument');
end;



function kk=isnodepresent(SS, NN)
% if node is present return it's position, otherwise return 0.
kk=0;
for ii=1:1:length(SS)
    if strcmp(SS{ii}, NN)==1
       kk=ii;
       break;
    end;
end;

