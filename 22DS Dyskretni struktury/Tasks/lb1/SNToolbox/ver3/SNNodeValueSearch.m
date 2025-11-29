function varargout = SNNodeValueSearch(varargin)
% SNNODEVALUESEARCH M-file for SNNodeValueSearch.fig
%      SNNODEVALUESEARCH, by itself, creates a new SNNODEVALUESEARCH or raises the existing
%      singleton*.
%
%      H = SNNODEVALUESEARCH returns the handle to a new SNNODEVALUESEARCH or the handle to
%      the existing singleton*.
%
%      SNNODEVALUESEARCH('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SNNODEVALUESEARCH.M with the given input arguments.
%
%      SNNODEVALUESEARCH('Property','Value',...) creates a new SNNODEVALUESEARCH or raises
%      the existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before SNNodeValueSearch_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to SNNodeValueSearch_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2004 The MathWorks, Inc.

% Edit the above text to modify the response to help SNNodeValueSearch

% Last Modified by GUIDE v2.5 30-Aug-2006 21:15:28

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @SNNodeValueSearch_OpeningFcn, ...
                   'gui_OutputFcn',  @SNNodeValueSearch_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT

% --- Executes just before SNNodeValueSearch is made visible.
function SNNodeValueSearch_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to SNNodeValueSearch (see VARARGIN)

% Choose default command line output for SNNodeValueSearch
handles.H=varargin{1};
MSL=handles.H.MSL;
SN=MSL(handles.H.LB);
handles.N=SN;
d=get(handles.H.popupmenu1,'Value');
h=SN.nodetype;
% Searchng question nodes
quest=[];
for i=find(h==0)
    b=0;
    for j=find(h==1)
        if isstr(SN.relation{i,j})
            if b==0
                quest(length(quest)+1)=i;
                mf(length(quest),1)=1;
                mf(length(quest),2)=j;
                b=1;
            else
                b=b+1;
                mf(length(quest),1)=mf(length(quest),1)+1;
                mf(length(quest),b+1)=j;
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
    for j=1:length(st)
        handles.outq(i,j)=st(j);
    end;
end;
handles.quest=quest;
handles.mf=mf;
handles.out=out;
handles.i=1;
handles.d=d;
handles.Answer=ones(size(handles.out));
handles.output = hObject;
draw(handles);
set(handles.H.figure1,'Visible','off');
% Update handles structure
guidata(hObject, handles);


% --- Outputs from this function are returned to the command line.
function varargout = SNNodeValueSearch_OutputFcn(hObject, eventdata, handles)
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Get default command line output from handles structure
varargout{1} = handles.output;



% --- Executes on selection change in listbox1.
function listbox1_Callback(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1


% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.i=1;
handles.Answer=ones(size(handles.out));
set(handles.listbox1,'String','');
set(handles.pushbutton1,'Enable','on');
draw(handles);
guidata(hObject, handles);

% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.H.figure1,'Visible','on');
delete(handles.figure1);

% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
S=get(handles.unitgroup,'SelectedObject');
if isempty(S)
    return;
end;
s=handles.mf(handles.i,1)-find(get(handles.unitgroup,'Children')==S)+1;
n=handles.mf(handles.i,s+1);
Rem=[];
for i=find(handles.Answer==1)
    if isempty(find(handles.outq(i,1:size(handles.outq,2))==n))
        b=1;
        for j=1:handles.mf(handles.i,1)
            if isempty(find(handles.outq(i,1:size(handles.outq,2))==handles.mf(handles.i,j+1)))
                b=0;
                break;
            end;
        end;
        if b==0
            Rem=[Rem handles.N.node{handles.out(i)} ', '];
            handles.Answer(i)=0;
        end;
    end;
end;
my_print(handles.listbox1, [Rem(1:length(Rem)-2) ' were removed'],get(handles.H.checkbox2,'Value'));
if isempty(find(handles.Answer==1))
    my_print(handles.listbox1, 'Sorry. No match there.',1);
    set(handles.pushbutton1,'Enable','off');
else
    my_print(handles.listbox1, [num2str(length(find(handles.Answer==1))) ' variants left'],get(handles.H.checkbox2,'Value'));
    my_print(handles.listbox1, '------------------------------------',get(handles.H.checkbox2,'Value'));
end;
if handles.i<length(handles.quest)
    handles.i=handles.i+1;
    draw(handles);
else
    if length(find(handles.Answer==1))>0
        my_print(handles.listbox1,[num2str(length(find(handles.Answer==1))) ' answers found:'],1);
    end;
    for i=find(handles.Answer==1)
        my_print(handles.listbox1,handles.N.node{handles.out(i)},1);
    end;
    set(handles.pushbutton1,'Enable','off');
end;
guidata(hObject, handles);


% --------------------------------------------------------------------
function unitgroup_SelectionChangeFcn(hObject, eventdata, handles)
% hObject    handle to unitgroup (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

function draw(handles);
C=get(handles.unitgroup,'Children');
for i=1:length(C)
    delete(C(i));
end;
x=[0.05 0.53];
ymin=0.1;
ymax=0.6;
n=handles.mf(handles.i,1);
dy=(ymax-ymin)./ceil(n./2);
for i=1:fix(n./2)
    uicontrol('Style','Radiobutton','Parent',handles.unitgroup,'Units','normalized','Position',[x(1) ymax-dy.*(i-1) 0.45 0.9.*dy],'String',handles.N.node{handles.mf(handles.i,2.*i)});
    uicontrol('Style','Radiobutton','Parent',handles.unitgroup,'Units','normalized','Position',[x(2) ymax-dy.*(i-1) 0.45 0.9.*dy],'String',handles.N.node{handles.mf(handles.i,2.*i+1)});
end;
if mod(n,2)==1
    uicontrol('Style','Radiobutton','Parent',handles.unitgroup,'Units','normalized','Position',[x(1) ymin 0.45 0.75.*dy],'String',handles.N.node{handles.mf(handles.i,n+1)});
end;
set(handles.unitgroup,'Title',[handles.N.node{handles.quest(handles.i)} '?'],'SelectedObject',[]);


% --- Executes when user attempts to close figure1.
function figure1_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
set(handles.H.figure1,'Visible','on');
% Hint: delete(hObject) closes the figure
delete(hObject);

function my_print(lb,s,b)
% it is my function to print string in listbox if trace is true
if b
    set(lb,'String',strvcat(get(lb,'String'),s));
end;
