function SN=SNaddORnode(varargin)
% Function Res=SNaddORnode(SN, 'node1', 'node2', ..., 'nodeN')
% adds nodes to the semantic network SN and return updated
% network to the Res variable
% ----------------------------------------------------------
% (C)(R) 2005 by S.A. Subbotin - http://www.uanis.nm.ru
if nargin>=2
   SN=varargin{1}; N3=length(SN.node); k=0;
   [N1 N2]=size(SN.relation);
   if N1==N2
      if N1==N3
         for i=1:1:nargin-1
             if isstr(varargin{i+1})==1
                flag=0;
                for j=1:1:N3+i-1-k
                    flag=flag+strcmp(SN.node{j},varargin{i+1});
                end;
                if flag==0
                   SN.node{N3+i-k}=varargin{i+1};
                   SN.relation{N3+i-k,N3+i-k}=[];
                   SN.nodetype(N3+i-k)=1;
                else
                   k=k+1;
   	           disp(strcat('Warning: The node [',varargin{i+1},'] is already exists in the node field'));
                end;
              else
                  k=k+1;
                  disp(strcat('Warning: The [',int2str(i+1),'-th] argument is ignored becouse it is not a string'));
              end;
         end; 
      else
          disp(strcat('Error: Node matrix is not correspond to relation matrix', int2str(N1),' x ', int2str(N3)));
      end;
   else
       disp(strcat('Error: Wrong relation matrix:', int2str(N1),' x ', int2str(N2)));
   end;
else
   disp('Error: The SNaddnode function must have more than 1 argument');
end;         