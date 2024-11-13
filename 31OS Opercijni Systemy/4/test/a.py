import win32api as wa
import win32file as wf

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
    print(d,dtn)