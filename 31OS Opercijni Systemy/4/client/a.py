import win32api as wa
import win32file as wf
from nicegui import ui

DRIVE_TYPES={
    wf.DRIVE_UNKNOWN:'UNKNOWN',
    wf.DRIVE_NO_ROOT_DIR:'NO_ROOT_DIR',
    wf.DRIVE_REMOVABLE:'REMOVABLE',
    wf.DRIVE_FIXED:'FIXED',
    wf.DRIVE_REMOTE:'REMOTE',
    wf.DRIVE_CDROM:'CDROM',
    wf.DRIVE_RAMDISK:'RAMDISK'
}

columns_data=[
    ('name','Name'),
    ('letter','Letter'),
    ('type','Type'),
    ('serial_number','Serial Number'),
    ('file_system','File System'),
    ('free_space','Free Space (GB)'),
    ('total_space','Total Space (GB)'),
]
columns=[
    {
        'name':data_name,
        'label':data_label,
        'field':data_name,
        'align':'left',
        'sortable':True
    }
    for data_name, data_label in columns_data
]
rows=[]

available_drives=[drive for drive in wa.GetLogicalDriveStrings().split('\000') if drive]
for drive_letter in available_drives:
    drive_type=DRIVE_TYPES[wf.GetDriveType(drive_letter)]
    drive_free_space,drive_total_space,_=[round(value*(10**-9)) for value in wf.GetDiskFreeSpaceEx(drive_letter)]
    drive_name,drive_serial_number,_,_,drive_file_system=wa.GetVolumeInformation(drive_letter)
    rows.append({
        'name':drive_name,
        'letter':drive_letter[:-2],
        'type':drive_type.capitalize(),
        'serial_number':drive_serial_number,
        'file_system':drive_file_system,
        'free_space':drive_free_space,
        'total_space':drive_total_space
    })

ui.table(columns=columns,rows=rows,row_key='name',title='Available Drives').classes('w-full')
ui.run(title="Операційні системи 4",favicon='💾')