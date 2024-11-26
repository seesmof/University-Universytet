function Res=SNdelnode(varargin)
% Function Res=SNdelnode(SN, 'node1', 'node2', ..., 'nodeN')
% delete nodes from the semantic network SN and return updated
% network to the Res variable
% ----------------------------------------------------------
% (C)(R) 2005 by S.A. Subbotin - http://www.uanis.nm.ru
if nargin>=2
   SN=varargin{1}; N3=length(SN.node); 
   [N1 N2]=size(SN.relation);
   if N1==N2
      if N1==N3
         for i=1:1:nargin-1
             if isstr(varargin{i+1})==1
                flag=isnodepresent(SN.node, varargin{i+1});
                if flag>0
                   SN.node{flag}=[];
                   for jjj=1:1:N1
                       SN.relation{flag,jjj}=[];
                       SN.relation{jjj,flag}=[];
                   end;
                else
   	           disp(strcat('Warning: The node [',varargin{i+1},'] is not exists in the node field'));
                end;
              else
                  disp(strcat('Warning: The [',int2str(i+1),'-th] argument is ignored becouse it is not a string'));
              end;
         end;
         Res=SNnew;
         ki=1;
         for i=1:1:N1
             if isstr(SN.node{i})==1             
                Res.node{ki}=SN.node{i};
                Res.nodetype(ki)=SN.nodetype(i);
                kj=1;
                for j=1:1:N1
                    if isstr(SN.node{j})==1
                       Res.relation{ki,kj}=SN.relation{i,j};
                       kj=kj+1;
                    end; 
                end;
                ki=ki+1;
             end;
         end;  
      else
          disp(strcat('Error: Node matrix is not correspond to relation matrix', int2str(N1),' x ', int2str(N3)));
      end;
   else
       disp(strcat('Error: Wrong relation matrix:', int2str(N1),' x ', int2str(N2)));
   end;
else
   disp('Error: The SNdelnode function must have more than 1 argument');
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

