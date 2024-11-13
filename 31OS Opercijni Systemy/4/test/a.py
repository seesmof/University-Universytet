import win32api as wa
import win32file as wf

from nicegui import ui

bytes_to_gigabyes=10**-9

drive_types={
    wf.DRIVE_UNKNOWN:'UNKNOWN',
    wf.DRIVE_NO_ROOT_DIR:'NO_ROOT_DIR',
    wf.DRIVE_REMOVABLE:'REMOVABLE',
    wf.DRIVE_FIXED:'FIXED',
    wf.DRIVE_REMOTE:'REMOTE',
    wf.DRIVE_CDROM:'CDROM',
    wf.DRIVE_RAMDISK:'RAMDISK'
}

cols=[
    {'name':'name','label':'Name','field':'name','align':'left','sortable':True},
    {'name':'letter','label':'Letter','field':'letter','align':'left','sortable':True},
    {'name':'type','label':'Type','field':'type','align':'left','sortable':True},
    {'name':'serial_number','label':'Serial Number','field':'serial_number','align':'left','sortable':True},
    {'name':'file_system','label':'File System','field':'file_system','align':'left','sortable':True},
    {'name':'free_space','label':'Free Space (GB)','field':'free_space','align':'left','sortable':True},
    {'name':'total_space','label':'Total Space (GB)','field':'total_space','align':'left','sortable':True},
]

rows=[]
available_drives=[drive for drive in wa.GetLogicalDriveStrings().split('\000') if drive]
for drive_letter in available_drives:
    drive_type=drive_types[wf.GetDriveType(drive_letter)]
    drive_free_space,drive_total_space,_=[round(value*bytes_to_gigabyes) for value in wf.GetDiskFreeSpaceEx(drive_letter)]
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

ui.table(columns=cols,rows=rows,row_key='name')
ui.run(title="Операційні системи 4",favicon='💾')