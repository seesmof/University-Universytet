function SNplot(SN, type, varargin)
% Function SNplot(SN, type, NodeColour, RelationColour) plot a semantic network structure for 
% SN variable 
% The plot type ('circle', 'random','hierarchy') must be specified
% with a type parameter
% The NodeColour and RelationColour parameters are not obligatory.
% ----------------------------------------------------------
% (C)(R) 2005 by S.A. Subbotin - http://www.uanis.nm.ru

%defaults
Plotprop.CircleRadius=0.5;
if nargin==2
   Plotprop.NodeColour='r'; Plotprop.RelationColour='b';  
end;
if nargin==3
   Plotprop.NodeColour=varargin{1};
   Plotprop.RelationColour='b';  
end;
if nargin>=4
   Plotprop.NodeColour=varargin{1};
   Plotprop.RelationColour=varargin{2};  
end;
   
if isstr(type)==1
   if length(SN.node)>1
       if strcmp(type, 'circle')==1
           SNcircleplot(SN, Plotprop);
       else
           if strcmp(type, 'random')==1
               SNrandomplot(SN, Plotprop);
           else
               if strcmp(type, 'hierarchy')==1
                   SNhierarchyplot(SN, Plotprop);
               else
                   disp('Error: The SNplot type is wrong. It can be circle, random or hierarchy');
               end;
           end;
       end;
   else
      disp('Error: The node field length is less then 2');
   end;
else
   disp('Error: The SNplot type must be a string');
end;
