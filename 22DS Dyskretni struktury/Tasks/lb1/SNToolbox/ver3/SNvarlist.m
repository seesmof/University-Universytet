% function Res=SNvarlist;
SNR='';
% who 
% whos global
SNTMP=whos('global');
for tmpi=1:1:length(SNTMP)
    SNTMP(tmpi).class
    if strcmp(SNTMP(tmpi).class,'struct')==1
        SNTMP(tmpi)
        if and((isfield(eval(SNTMP(tmpi).name),'node')==1),and(isfield(eval(SNTMP(tmpi).name),'relation'),isfield(eval(SNTMP(tmpi).name),'nodetype')))
           SNR=strcat(SNR, SNTMP(tmpi).name);  
        end;    
    end; % if
end;
Res=SNR;
global Res