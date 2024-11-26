function varargout = SNEditNode(varargin)
% SNEDITNODE M-file for SNEditNode.fig
%      SNEDITNODE, by itself, creates a new SNEDITNODE or raises the existing
%      singleton*.
%
%      H = SNEDITNODE returns the handle to a new SNEDITNODE or the handle to
%      the existing singleton*.
%
%      SNEDITNODE('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SNEDITNODE.M with the given input arguments.
%
%      SNEDITNODE('Property','Value',...) creates a new SNEDITNODE or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before SNEditNode_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to SNEditNode_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help SNEditNode

% Last Modified by GUIDE v2.5 11-Aug-2006 00:33:28

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @SNEditNode_OpeningFcn, ...
                   'gui_OutputFcn',  @SNEditNode_OutputFcn, ...
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


% --- Executes just before SNEditNode is made visible.
function SNEditNode_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to SNEditNode (see VARARGIN)
handles.H=varargin{1};
MSL=handles.H.MSL;
Q=MSL(handles.H.LB);
handles.N=Q;
set(handles.listbox1,'String',Q.node);
handles.S=sign(length(Q.node));
if length(Q.node)>0
    set(handles.listbox1,'Value',1);
    set(handles.radiobutton2,'Value',Q.nodetype(1));
    set(handles.radiobutton1,'Value',1-Q.nodetype(1));
else
    set(handles.uipanel1,'Visible','off');
end;
set(handles.H.figure1,'Visible','off');
% Choose default command line output for SNEditNode
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes SNEditNode wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = SNEditNode_OutputFcn(hObject, eventdata, handles) 
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
if handles.S>0
    handles.S=get(handles.listbox1,'Value');
    Q=handles.N;
    set(handles.radiobutton2,'Value',Q.nodetype(handles.S));
    set(handles.radiobutton1,'Value',1-Q.nodetype(handles.S));
    %%
    handles.output = hObject;
    guidata(hObject, handles);
end
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


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
N=handles.N;
name='Add new node'; prompt={'Enter node name name'}; numlines=1;
answer=char(inputdlg(prompt,name,numlines));
if ~isempty(answer)
    if isempty(get(handles.listbox1,'String'))
        N=SNaddANDnode(N,answer);
        handles.N=N;
        set(handles.listbox1,'String',{answer},'Value',1);
        handles.S=1;
        set(handles.uipanel1,'Visible','on');
        set(handles.radiobutton2,'Value',0);
        set(handles.radiobutton1,'Value',1);
    else
        z=get(handles.listbox1,'String');
        if strcmp(z,answer)==zeros(size(z))
            N=SNaddANDnode(N,answer);
            handles.N=N;
            set(handles.listbox1,'String',[z;{answer}],'Value',1);
            handles.S=1;
        else
            errordlg('The node with this name is already exists!','Error');
        end;
    end;
end;
% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.S>0
    qwe=get(handles.listbox1,'String');
    handles.N=SNdelnode(handles.N,char(qwe(handles.S)));
    qwe(handles.S)=[];
    if size(qwe,1)+1==handles.S
        set(handles.listbox1,'Value',handles.S-1);
        handles.S=handles.S-1;
    end
    if isempty(qwe)
        handles.S=0;
        set(handles.uipanel1,'Visible','off');
    end;
    set(handles.listbox1,'String',qwe);
end;
% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.S>0
    name='Rename node'; prompt={'Enter new name'}; numlines=1;
    answer=char(inputdlg(prompt,name,numlines));
    if ~isempty(answer)
        z=get(handles.listbox1,'String');
        if strcmp(z,answer)==zeros(size(z))
            z(handles.S)={answer};
            handles.N.node(handles.S)={answer};
            set(handles.listbox1,'String',z);
        else
            errordlg('The node this name is already exists!','Error');
        end;
    end;
end;
% Update handles structure
guidata(hObject, handles);



% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Q=handles.N;
Q.nodetype(handles.S)=0;
handles.N=Q;
guidata(hObject, handles);
% Hint: get(hObject,'Value') returns toggle state of radiobutton1




% --- Executes when user attempts to close figure1.
function figure1_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Hint: delete(hObject) closes the figure
delete(hObject);




% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Q=handles.N;
Q.nodetype(handles.S)=1;
handles.N=Q;

guidata(hObject, handles);
% Hint: get(hObject,'Value') returns toggle state of radiobutton2



% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
handles.H.MSL(handles.H.LB)=handles.N;
guidata(handles.H.output,handles.H);
set(handles.H.figure1,'Visible','on');
delete(handles.figure1);