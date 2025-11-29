function varargout = SNTool(varargin)
% SNTOOL M-file for SNTool.fig
%      SNTOOL, by itself, creates a new SNTOOL or raises the existing
%      singleton*.
%
%      H = SNTOOL returns the handle to a new SNTOOL or the handle to
%      the existing singleton*.
%
%      SNTOOL('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SNTOOL.M with the given input arguments.
%
%      SNTOOL('Property','Value',...) creates a new SNTOOL or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before SNTool_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to SNTool_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help SNTool

% Last Modified by GUIDE v2.5 25-Sep-2006 12:53:55

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @SNTool_OpeningFcn, ...
                   'gui_OutputFcn',  @SNTool_OutputFcn, ...
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


% --- Executes just before SNTool is made visible.
function SNTool_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to SNTool (see VARARGIN)
q(1)=SNnew;
q(1)=[];
handles.MSL=q;
handles.LB=0;
% Choose default command line output for SNTool
handles.output = hObject;

% my_update handles structure
guidata(hObject, handles);

% UIWAIT makes SNTool wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = SNTool_OutputFcn(hObject, eventdata, handles) 
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

if isempty(get(handles.listbox1,'String'))
    handles.LB=0;
else
    handles.LB=get(handles.listbox1,'Value');
    if isempty(handles.MSL(handles.LB).node)
        set(handles.popupmenu1,'String',char(13),'Value',1);
    else
        set(handles.popupmenu1,'String',handles.MSL(handles.LB).node,'Value',1);
    end;
end;
% Update handles structure
guidata(hObject, handles);
%The end

% Hints: contents = get(hObject,'String') returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1


% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called
%**
%*****
%set(hObject,'String',Res);


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
MSL=handles.MSL;
name='Add new network'; prompt={'Enter semantic network name'}; numlines=1;
answer=char(inputdlg(prompt,name,numlines));
if ~isempty(answer)
    if isempty(get(handles.listbox1,'String'))
        MSL(1)=SNnew;
        handles.MSL=MSL;
        set(handles.listbox1,'String',{answer},'Value',1);
        handles.LB=1;
    else
        z=get(handles.listbox1,'String');
        if strcmp(z,answer)==zeros(size(z))
            MSL(size(MSL)+1)=SNnew;
            handles.MSL=MSL;
            set(handles.listbox1,'String',[z;{answer}],'Value',1);
            handles.LB=1;
        else
            errordlg('The network variable with this name is already exists!','Error');
        end;
    end;
end;
my_update(handles);
% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    qwe=get(handles.listbox1,'String');
    b=questdlg(['Are you realy want to remove the network ' char(qwe(handles.LB))],'Confirmation');
    if strcmp(b,'Yes')
        handles.MSL(handles.LB)=[];
        qwe(handles.LB)=[];
        if size(qwe,1)+1==handles.LB
            set(handles.listbox1,'Value',handles.LB-1);
            handles.LB=handles.LB-1;
        end
        if isempty(qwe)
            handles.LB=0;
        end;
        set(handles.listbox1,'String',qwe);
        my_update(handles);
        % Update handles structure
        guidata(hObject, handles);
        %The end
    end;
end;

% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    q=handles.MSL(handles.LB);
    if length(q.node)>1
        S=get(handles.listbox1,'String');
        F=figure('Color',[1 1 1],'Name',['Hierarchy plot of ' char(S(handles.LB))],'NumberTitle','off');
        A=axes('Parent',F,'XColor',[1 1 1],'YColor',[1 1 1]);
        SNplot(q,'hierarchy');
    end;
end;

% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    q=handles.MSL(handles.LB);
    if length(q.node)>1
        S=get(handles.listbox1,'String');
        F=figure('Color',[1 1 1],'Name',['Circle plot of ' char(S(handles.LB))],'NumberTitle','off');
        A=axes('Parent',F,'XColor',[1 1 1],'YColor',[1 1 1]);        
        SNplot(q,'circle');
    end;
end;

% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    q=handles.MSL(handles.LB);
    if length(q.node)>1
        S=get(handles.listbox1,'String');
        F=figure('Color',[1 1 1],'Name',['Random plot of ' char(S(handles.LB))],'NumberTitle','off');
        A=axes('Parent',F,'XColor',[1 1 1],'YColor',[1 1 1]);        
        SNplot(q,'random');
    end;
end;

% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    SNEditNode(handles);
    %update(handles);
end
% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton7.
function pushbutton7_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton7 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    if length(handles.MSL(handles.LB).node)>1
        SNEditRelation(handles);
    else
        warndlg('Add nodes before adding relations','Warning');
    end;
end;
% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton9.
function pushbutton9_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    MSL=handles.MSL;
    name='Duplicate selected network'; prompt={'Enter semantic network name'}; numlines=1;
    answer=char(inputdlg(prompt,name,numlines));
    if ~isempty(answer)
        z=get(handles.listbox1,'String');
        if strcmp(z,answer)==zeros(size(z))
            MSL(size(MSL)+1)=MSL(handles.LB);
            handles.MSL=MSL;
            set(handles.listbox1,'String',[z;{answer}]);
        else
            errordlg('The network variable with this name is already exists!','Error');
        end;
    end;
end;
my_update(handles);
guidata(hObject, handles);
%The end

% --- Executes on button press in pushbutton10.
function pushbutton10_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton10 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    name='Rename network'; prompt={'Enter new name'}; numlines=1;
    answer=char(inputdlg(prompt,name,numlines));
    if ~isempty(answer)
        z=get(handles.listbox1,'String');
        if strcmp(z,answer)==zeros(size(z))
            z(handles.LB)={answer};
            set(handles.listbox1,'String',z);
        else
            errordlg('The network variable with this name is already exists!','Error');
        end;
    end;
end;
my_update(handles);
% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in pushbutton11.
function pushbutton11_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton11 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if (handles.LB>0)&(length(get(handles.popupmenu1,'String'))>1)
    SNNodeValueSearch(handles);
end
% Update handles structure
guidata(hObject, handles);


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in checkbox2.
function checkbox2_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox2


% --- Executes on button press in pushbutton15.
function pushbutton15_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton15 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    SN=handles.MSL(get(handles.popupmenu2,'Value'));
    SN1=handles.MSL(get(handles.popupmenu3,'Value'));
    Res=SNfind(SN,SN1,get(handles.checkbox3,'Value'));
    if isempty(Res)
        msgbox('Solution not found');
    else
        msgbox(['Result is ' char(Res)]);
    end;
end;

% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2


% --- Executes during object creation, after setting all properties.
function popupmenu2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in checkbox3.
function checkbox3_Callback(hObject, eventdata, handles)
% hObject    handle to checkbox3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of checkbox3


% --- Executes on selection change in popupmenu3.
function popupmenu3_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns popupmenu3 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu3


% --- Executes during object creation, after setting all properties.
function popupmenu3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton16.
function pushbutton16_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton16 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
%msgbox('Call 911. They will help you');

% --- Executes on button press in pushbutton17.
function pushbutton17_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton17 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
SNabout;

% --- Executes on button press in pushbutton19.
function pushbutton19_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton19 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    [fname, pname] = uiputfile({'*.kb'},'Enter filename, you want to save');
    if ~isempty(fname)&(ischar(fname))
        SN=handles.MSL(handles.LB);
        SN2E2Go(SN,[pname fname]);
        Q=get(handles.listbox1,'String');
        msgbox(['The network ' char(Q(handles.LB)) ' is converted into E2Go knowledge base. Press OK']);
    end;
end;

% --- Executes on button press in pushbutton20.
function pushbutton20_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton20 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[fname, pname] = uigetfile({'*.mat'},'Pick a file');
if ~isempty(fname)&ischar(fname)
    if exist([pname fname])==2
        load([pname fname]);
        if exist('SN')&(exist('name')==1)&(isstr(name))
            MSL=handles.MSL;
            z=get(handles.listbox1,'String');
            if handles.LB==0
                MSL(1)=SN;
                handles.MSL=MSL;
                set(handles.listbox1,'String',{name});
                handles.LB=1;
            else
                if strcmp(z,name)==zeros(size(z))
                    MSL(size(MSL)+1)=SN;
                    handles.MSL=MSL;
                    set(handles.listbox1,'String',[z;{name}]);
                else
                    errordlg('The network variable with this name is already exists,delete it before loading!','Error');
                end;
            end;
        end;
        my_update(handles);
        guidata(hObject, handles);
    end;
end;

% --- Executes on button press in pushbutton21.
function pushbutton21_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton21 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    [fname, pname] = uiputfile({'*.mat'},'Pick a file');
    if ~isempty(fname)&ischar(fname)
        SN=handles.MSL(handles.LB);
        S=get(handles.listbox1,'String');
        name=S{handles.LB};
        save([pname fname],'name','SN');
    end;
end;


function my_update(handles)
if handles.LB>0
    set(handles.popupmenu2,'String',get(handles.listbox1,'String'));
    set(handles.popupmenu3,'String',get(handles.listbox1,'String'));
    if size(get(handles.listbox1,'String'),1)<get(handles.popupmenu2,'Value')
        set(handles.popupmenu2,'Value',1);
    end;
    if size(get(handles.listbox1,'String'),1)<get(handles.popupmenu3,'Value')
        set(handles.popupmenu3,'Value',1);
    end;
    if isempty(handles.MSL(handles.LB).node)
        set(handles.popupmenu1,'String',char(13),'Value',1);
    else
        set(handles.popupmenu1,'String',handles.MSL(handles.LB).node,'Value',1);
    end;
else
    set(handles.popupmenu2,'String',char(13),'Value',1);
    set(handles.popupmenu3,'String',char(13),'Value',1);
    set(handles.popupmenu1,'String',char(13),'Value',1);
end;


% --- Executes on button press in pushbutton18.
function pushbutton18_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton18 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
if handles.LB>0
    [fname, pname] = uiputfile({'*.fis'},'Enter filename, you want to save');
    if ~isempty(fname)&(ischar(fname))
        SN=handles.MSL(handles.LB);
        S=get(handles.listbox1,'String');
        SN2Fis(SN,[pname fname],S{handles.LB});
        Q=get(handles.listbox1,'String');
        msgbox(['The network ' char(Q(handles.LB)) ' is converted into Fis knowledge base. Press OK']);
    end;
end;