function varargout = SNabout(varargin)
% SNABOUT M-file for SNabout.fig
%      SNABOUT, by itself, creates a new SNABOUT or raises the existing
%      singleton*.
%
%      H = SNABOUT returns the handle to a new SNABOUT or the handle to
%      the existing singleton*.
%
%      SNABOUT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SNABOUT.M with the given input arguments.
%
%      SNABOUT('Property','Value',...) creates a new SNABOUT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before SNabout_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to SNabout_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help SNabout

% Last Modified by GUIDE v2.5 09-Apr-2006 13:55:40

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @SNabout_OpeningFcn, ...
                   'gui_OutputFcn',  @SNabout_OutputFcn, ...
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


% --- Executes just before SNabout is made visible.
function SNabout_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to SNabout (see VARARGIN)

% Choose default command line output for SNabout
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes SNabout wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = SNabout_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton5.
function pushbutton5_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


