function varargout = SNEditRelation(varargin)
% SNEDITRELATION M-file for SNEditRelation.fig
%      SNEDITRELATION, by itself, creates a new SNEDITRELATION or raises the existing
%      singleton*.
%
%      H = SNEDITRELATION returns the handle to a new SNEDITRELATION or the handle to
%      the existing singleton*.
%
%      SNEDITRELATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SNEDITRELATION.M with the given input arguments.
%
%      SNEDITRELATION('Property','Value',...) creates a new SNEDITRELATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before SNEditRelation_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to SNEditRelation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help SNEditRelation

% Last Modified by GUIDE v2.5 01-Sep-2006 00:40:03

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @SNEditRelation_OpeningFcn, ...
                   'gui_OutputFcn',  @SNEditRelation_OutputFcn, ...
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


% --- Executes just before SNEditRelation is made visible.
function SNEditRelation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to SNEditRelation (see VARARGIN)
handles.H=varargin{1};
MSL=handles.H.MSL;
Q=MSL(handles.H.LB);
handles.N=Q;
handles.L=1;
handles.R=1;
set(handles.Left,'String',Q.node,'Value',1);
set(handles.Right,'String',Q.node,'Value',1);
List=[];
RT={};
for i=1:length(Q.node)
    for j=1:length(Q.node)
        if isstr(Q.relation{i,j})
            set(handles.listbox4,'String',strvcat(get(handles.listbox4,'String'),[Q.node{i} ' ' Q.relation{i,j} ' ' Q.node{j}]));
            List(size(List,1)+1,1)=i;
            List(size(List,1),2)=j;
            b=0;
            for k=1:length(RT)
                if strcmp(RT{k},Q.relation{i,j})
                    b=1;
                    break;
                end;
            end;
            if b==0
                RT{length(RT)+1}=Q.relation{i,j};
            end;
        end;
    end;
end;
handles.List=List;
if length(RT)>0
    set(handles.listbox3,'String',RT,'Value',1);
else
    set(handles.listbox3,'String',{char(13)},'Value',1);
end;
set(handles.H.figure1,'Visible','off');

% Choose default command line output for SNEditRelation
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes SNEditRelation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = SNEditRelation_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in Left.
function Left_Callback(hObject, eventdata, handles)
% hObject    handle to Left (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.L=get(handles.Left,'Value');
if (handles.L~=handles.R)&(isempty(handles.N.relation{handles.L,handles.R}))
    set(handles.listbox3,'Enable','on');
else
    set(handles.listbox3,'Enable','off');
end;
guidata(hObject, handles);
% Hints: contents = get(hObject,'String') returns Left contents as cell array
%        contents{get(hObject,'Value')} returns selected item from Left


% --- Executes during object creation, after setting all properties.
function Left_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Left (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in Right.
function Right_Callback(hObject, eventdata, handles)
% hObject    handle to Right (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.R=get(handles.Right,'Value');
if (handles.L~=handles.R)&(isempty(handles.N.relation{handles.L,handles.R}))
    set(handles.listbox3,'Enable','on');
else
    set(handles.listbox3,'Enable','off');
end;
guidata(hObject, handles);
% Hints: contents = get(hObject,'String') returns Right contents as cell array
%        contents{get(hObject,'Value')} returns selected item from Right


% --- Executes during object creation, after setting all properties.
function Right_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Right (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



% --- Executes when user attempts to close figure1.
function figure1_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.H.MSL(handles.H.LB)=handles.N;
guidata(handles.H.output,handles.H);
set(handles.H.figure1,'Visible','on');
% Hint: delete(hObject) closes the figure
delete(hObject);




% --- Executes on selection change in listbox3.
function listbox3_Callback(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox3


% --- Executes during object creation, after setting all properties.
function listbox3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox3.
function listbox4_Callback(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox3


% --- Executes during object creation, after setting all properties.
function listbox4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox4.
function listbox6_Callback(hObject, eventdata, handles)
% hObject    handle to listbox4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns listbox4 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox4


% --- Executes during object creation, after setting all properties.
function listbox6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if size(handles.List,1)==0
    return;
end;
if strcmp('Yes',questdlg('Are you sure that you want to delete a relation'))==0
    return;
end;
q=get(handles.listbox4,'Value');
S=get(handles.listbox4,'String');
S=[S(1:(q-1),1:size(S,2));S((q+1):size(S,1),1:size(S,2))];
set(handles.listbox4,'String',S,'Value',1);
handles.N.relation{handles.List(q,1),handles.List(q,2)}=[];
handles.List=[handles.List(1:q-1,1:2);handles.List(q+1:size(handles.List,1),1:2)];
guidata(hObject, handles);

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if strcmp('Yes',questdlg('Are you sure that you want to delete all relations'))==0
    return;
end;
for q=1:size(handles.List,1)
    handles.N.relation{handles.List(q,1),handles.List(q,2)}=[];
end;
set(handles.listbox4,'String',char(0));
handles.List=[];
guidata(hObject, handles);

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
answer=char(inputdlg({'Enter relation type'}));
if ~isempty(answer)
    RT=get(handles.listbox3,'String');
    if strcmp(char(RT{1}),char(13))
        set(handles.listbox3,'String',{answer},'Value',1);
        return;
    end;
    b=0;
    for k=1:length(RT)
        if strcmp(RT{k},answer)
            b=1;
            break;
        end;
    end;
    if b==0
        RT{length(RT)+1}=answer;
        set(handles.listbox3,'String',RT,'Value',1);
    end;
end;

    
    
% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
RT=get(handles.listbox3,'String');
if strcmp(RT{1},char(13))
    return;
end;
if (handles.L==handles.R)|(isstr(handles.N.relation{handles.L,handles.R}))
    return;
end;
handles.N.relation{handles.L,handles.R}=RT{get(handles.listbox3,'Value')};
set(handles.listbox4,'String',strvcat(get(handles.listbox4,'String'),[handles.N.node{handles.L} ' ' handles.N.relation{handles.L,handles.R} ' ' handles.N.node{handles.R}]));
if ~isempty(handles.List)
    hanldes.List(size(handles.List,1)+1,1)=handles.L;
    handles.List(size(handles.List,1),2)=handles.R;
else
    hanldes.List(1,1)=handles.L;
    handles.List(1,2)=handles.R;
end;
guidata(hObject, handles);

% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.H.MSL(handles.H.LB)=handles.N;
guidata(handles.H.output,handles.H);
set(handles.H.figure1,'Visible','on');
delete(handles.figure1);