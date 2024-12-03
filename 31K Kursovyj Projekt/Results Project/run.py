from datetime import datetime
from nicegui import ui
import platform
import psutil
import win32api

'''
processor 
    name 
    clock speed 
    cores 
    threads 
    temperature 
'''

def get_formatted_size(bytes,suffix='B'):
    '''
    Scale bytes to proper format 
        1253656 > '1.20MB'
        1253656678 > '1.17GB'
    '''
    factor=1024
    for unit in ['','K','M','G','T','P']:
        if bytes<factor: return f'{bytes:.2f} {unit}{suffix}'
        bytes/=factor

print()
uname=platform.uname()
print('system',uname.system)
print('node name',uname.node)
print('release',uname.release)
print('version',uname.version)
print('machine',uname.machine)
print('processor',uname.processor)
# TODO get cpu name using cpuinfo probably JESUS please help 

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

print()
system_virtual_memory=psutil.virtual_memory()
print('total',get_formatted_size(system_virtual_memory.total))
print('available',get_formatted_size(system_virtual_memory.available))
print('used',get_formatted_size(system_virtual_memory.used))
print('percentage',f'{system_virtual_memory.percent}%')
swap=psutil.swap_memory()
print('total',get_formatted_size(swap.total))
print('free',get_formatted_size(swap.free))
print('used',get_formatted_size(swap.used))
print('percentage',f'{swap.percent}%')

print()
partitions=psutil.disk_partitions()
for partition in partitions:
    print('device',partition.device)
    print('mountpoint',partition.mountpoint)
    drive_name=win32api.GetVolumeInformation(partition.device)[0]
    print('name',drive_name)
    print('file system type',partition.fstype)
    try: partition_usage=psutil.disk_usage(partition.mountpoint)
    except: continue
    print('total',get_formatted_size(partition_usage.total))
    print('used',get_formatted_size(partition_usage.used))
    print('free',get_formatted_size(partition_usage.free))
    print('percentage',f'{partition_usage.percent}%')
disk_io=psutil.disk_io_counters()
print('total read',get_formatted_size(disk_io.read_bytes))
print('total write',get_formatted_size(disk_io.write_bytes))

print()
if_addrs=psutil.net_if_addrs()
for interface_name,interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(interface_name,address.family.name)
        if address.family.name=='AF_INET':
            print('ip address',address.address)
            print('netmask',address.netmask)
            print('broadcast ip',address.broadcast)
        elif address.family.name=='AF_PACKET':
            print('mac address',address.address)
            print('netmask',address.netmask)
            print('broadcast mac',address.broadcast)
net_io=psutil.net_io_counters()
print('total bytes sent',get_formatted_size(net_io.bytes_sent))
print('total bytes received',get_formatted_size(net_io.bytes_recv))

def update_ui():
    system_data['type']=uname.system
    system_data['user']=uname.node
    system_table.rows=[{'property':k.capitalize(),'value':v} for k,v in system_data.items()]

HEADING_CLASSES='font-bold text-xl'
with ui.row().classes('flex gap-3'):
    with ui.column():
        system_data={
            'type':uname.system,
            'user':uname.node,
            'release':uname.release,
            'version':uname.version,
            'machine':uname.machine,
        }
        system_table_rows=[{'property':k.capitalize(),'value':v} for k,v in system_data.items()]
        system_table_columns=[
            {'name':'property','label':'Property','field':'property'},
            {'name':'value','label':'Value','field':'value'},
        ]
        system_table=ui.table(columns=system_table_columns,rows=system_table_rows,row_key='name',title='System')
        boot_time_label=ui.label(f'Booted: {boot_time.day}.{boot_time.month}.{boot_time.year} {boot_time.hour:02d}:{boot_time.minute:02d}:{boot_time.second:02d}')
    with ui.column():
        processor_data={
            'name':uname.processor,
        }
        processor_table_rows=[{'property':k.capitalize(),'value':v} for k,v in processor_data.items()]
        processor_table_columns=[
            {'name':'property','label':'Property','field':'property'},
            {'name':'value','label':'Value','field':'value'},
        ]
        processor_table=ui.table(columns=processor_table_columns,rows=processor_table_rows,row_key='name',title='Processor')
    with ui.column():
        ui.label('Memory').classes(HEADING_CLASSES)
        ui.label('Name')
    with ui.column():
        ui.label('Disks').classes(HEADING_CLASSES)
        ui.label('Name')
    with ui.column():
        ui.label('Network').classes(HEADING_CLASSES)
        ui.label('Name')

ui.timer(1,update_ui,active=True)
ui.run()
