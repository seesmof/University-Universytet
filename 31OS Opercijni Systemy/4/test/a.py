import win32api as wa
import win32file as wf

B_TO_GB=10**-9

dts={
    wf.DRIVE_UNKNOWN:'UNKNOWN',
    wf.DRIVE_NO_ROOT_DIR:'NO_ROOT_DIR',
    wf.DRIVE_REMOVABLE:'REMOVABLE',
    wf.DRIVE_FIXED:'FIXED',
    wf.DRIVE_REMOTE:'REMOTE',
    wf.DRIVE_CDROM:'CDROM',
    wf.DRIVE_RAMDISK:'RAMDISK'
}

ds=[d for d in wa.GetLogicalDriveStrings().split('\000') if d]
for d in ds:
    dt=wf.GetDriveType(d)
    dtn=dts[dt]
    drive_free_space,drive_total_space,_=wf.GetDiskFreeSpaceEx(d)
    drive_free_space=round(drive_free_space*B_TO_GB)
    drive_total_space=round(drive_total_space*B_TO_GB)
    print(d,drive_free_space,drive_total_space)