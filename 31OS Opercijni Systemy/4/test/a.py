import win32api as wa
import win32file as wf

ds=[d for d in wa.GetLogicalDriveStrings().split('\000') if d]
for d in ds:
    dt=wf.GetDriveType(d)
    print(d,dt)