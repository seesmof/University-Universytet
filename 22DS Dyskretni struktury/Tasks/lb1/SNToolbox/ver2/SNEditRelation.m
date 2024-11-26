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

% Last Modified by GUIDE v2.5 16-Jul-2006 17:45:54

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
set(handles.Left,'String',Q.node);
set(handles.Right,'String',Q.node);
handles.L=1;
handles.R=1;
set(handles.Left,'Value',1);
set(handles.Right,'Value',1);
set(handles.edit1,'Enable','off');
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
if handles.L==handles.R
    set(handles.edit1,'Enable','off');
    set(handles.edit1,'String','');
else
    if isempty(handles.N.relation(handles.L,handles.R))
        set(handles.edit1,'String','');
    else
        set(handles.edit1,'String',handles.N.relation(handles.L,handles.R));
    end;
    set(handles.edit1,'Enable','on');
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
if handles.L==handles.R
    set(handles.edit1,'String','');
    set(handles.edit1,'Enable','off');
else
    if isempty(handles.N.relation(handles.L,handles.R))
        set(handles.edit1,'String','');
    else
        set(handles.edit1,'String',handles.N.relation(handles.L,handles.R));
    end;
    set(handles.edit1,'Enable','on');
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



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
Q=get(handles.edit1,'String');
if isempty(Q{1});
    handles.N.relation{handles.L,handles.R}=[];
else
    handles.N.relation{handles.L,handles.R}=Q{1};
end;
guidata(hObject, handles);
% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
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


