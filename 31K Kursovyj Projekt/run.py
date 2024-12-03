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

print()
print('physical cores',psutil.cpu_count(logical=False))
print('total cores',psutil.cpu_count(logical=True))
cpu_frequency=psutil.cpu_freq()
print('max frequency',f'{cpu_frequency.max:.2f}MHz')
print('min frequency',f'{cpu_frequency.min:.2f}MHz')
print('current frequency',f'{cpu_frequency.current:.2f}MHz')
print('cpu usage per core')
for i,percentage in enumerate(psutil.cpu_percent(percpu=True,interval=1)):
    print('core',i,f'{percentage}%')
print('total cpu usage',f'{psutil.cpu_percent()}%')

ui.run()