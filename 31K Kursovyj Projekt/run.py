from datetime import datetime
from nicegui import ui
import platform
import psutil

'''
processor 
    name 
    clock speed 
    cores 
    threads 
    temperature 
'''

def get_size(bytes,suffix='B'):
    '''
    Scale bytes to proper format 
        1253656 > '1.20MB'
        1253656678 > '1.17GB'
    '''
    factor=1024
    for unit in ['','K','M','G','T','P']:
        if bytes<factor: return f'{bytes:.2f}{unit}{suffix}'
        bytes/=factor

print()
uname=platform.uname()
print('system',uname.system)
print('node name',uname.node)
print('release',uname.release)
print('version',uname.version)
print('machine',uname.machine)
print('processor',uname.processor)

print()
boot_time_stamp=psutil.boot_time()
boot_time=datetime.fromtimestamp(boot_time_stamp)
print('boot time',f'{boot_time.day}.{boot_time.month}.{boot_time.year} {boot_time.hour:02d}:{boot_time.minute:02d}:{boot_time.second:02d}')

ui.run()