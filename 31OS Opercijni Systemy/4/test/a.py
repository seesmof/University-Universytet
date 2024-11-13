import win32api as wa
import win32file as wf
import subprocess as sp
import wmi

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

available_drives=[drive for drive in wa.GetLogicalDriveStrings().split('\000') if drive]
for drive in available_drives:
    drive_type=drive_types[wf.GetDriveType(drive)]
    drive_free_space,drive_total_space,_=[round(value*bytes_to_gigabyes) for value in wf.GetDiskFreeSpaceEx(drive)]
    drive_name,drive_serial_number,_,_,drive_file_system=wa.GetVolumeInformation(drive)