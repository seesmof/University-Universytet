function Res=SNaddrelation(SN, node1, relation, node2)
% Function Res=SNaddrelation(SN, node1, relation, node2)
% adds a relation between the node1 and the node2 nodes
% to the semantic network SN and return updated
% network to the Res variable
% ----------------------------------------------------------
% (C)(R) 2005 by S.A. Subbotin - http://www.uanis.nm.ru
if nargin==4
   if and(and(and(isstr(node1)==1,isstr(node2)==1), isstr(relation)==1), and(strcmp(node1, node2)==0, and(strcmp(node2, relation)==0, strcmp(node1, relation)==0)))
      n1=isnodepresent(SN.node, node1);
      if n1>0
         n2=isnodepresent(SN.node, node2);
         if n2>0
             SN.relation{n1,n2}=relation;
             Res=SN;
         else
             disp(strcat('Error: The node [',node2,'] is absent in the node field'));     
         end;
      else
          disp(strcat('Error: The node [',node1,'] is absent in the node field'));     
      end;
   else
      disp('Error: Wrong arguments! There are must be 3 different strings.');     
   end;
else
   disp('Error: Wrong number of arguments! There are must be 4 arguments.');
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

