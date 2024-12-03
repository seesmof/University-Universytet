from collections import defaultdict
from datetime import datetime
from nicegui import ui
import platform
import psutil
import win32api

HEADING_CLASSES='font-bold text-xl'
COLUMNS=[
    {'name':'property','label':'Property','field':'property','align':'left'},
    {'name':'value','label':'Value','field':'value','sortable':True},
]

# TODO get cpu name using cpuinfo probably JESUS please help 
uname=platform.uname()
boot_time_stamp=psutil.boot_time()
boot_time=datetime.fromtimestamp(boot_time_stamp)
cpu_frequency=psutil.cpu_freq()
system_virtual_memory=psutil.virtual_memory()
swap=psutil.swap_memory()
partitions=psutil.disk_partitions()
disk_io=psutil.disk_io_counters()
if_addrs=psutil.net_if_addrs()
net_io=psutil.net_io_counters()

def get_rows(data:dict):
    return [{'property':k.capitalize(),'value':v} for k,v in data.items()]

def update_ui():
    processor_frequencies_data={
        'min':cpu_frequency.min,
        'max':cpu_frequency.max,
        'current':cpu_frequency.current,
    }
    processor_frequencies_table.rows=get_rows(processor_frequencies_data)

    cpu_usage=psutil.cpu_percent(percpu=True)
    # TODO add color highlight on higher usage: yellow if more than 60% and red if more than 77%
    # user query tool here somehow JESUS please help 
    processor_usage_data={
        f'Core {i}': usage
        for i,usage in enumerate(cpu_usage)
    }
    processor_usage_table.rows=get_rows(processor_usage_data)

    cpu_usage=psutil.cpu_percent()
    x=datetime.now().timestamp()
    processor_usage_plot.push([x],[[cpu_usage]])

    system_virtual_memory=psutil.virtual_memory()
    virtual_memory_data={
        'total':get_formatted_size(system_virtual_memory.total),
        'available':get_formatted_size(system_virtual_memory.available),
        'used':get_formatted_size(system_virtual_memory.used),
        'percentage':f'{system_virtual_memory.percent}%',
    }
    virtual_memory_table.rows=get_rows(virtual_memory_data)

    swap=psutil.swap_memory()
    swap_memory_data={
        'total':get_formatted_size(swap.total),
        'free':get_formatted_size(swap.free),
        'used':get_formatted_size(swap.used),
        'percentage':f'{swap.percent}%',
    }
    swap_memory_table.rows=get_rows(swap_memory_data)

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

with ui.row().classes('flex gap-3'):
    with ui.column():
        system_data={
            'type':uname.system,
            'user':uname.node,
            'release':uname.release,
            'version':uname.version,
            'machine':uname.machine,
            'booted':f'{boot_time.day}.{boot_time.month}.{boot_time.year} {boot_time.hour:02d}:{boot_time.minute:02d}:{boot_time.second:02d}'
        }
        system_table=ui.table(columns=COLUMNS,rows=get_rows(system_data),row_key='name',title='System')
    with ui.column():
        processor_data={
            'name':uname.processor,
            'platform':uname.machine,
            'cores':psutil.cpu_count(logical=False),
            'threads':psutil.cpu_count(logical=True),
        }
        processor_table=ui.table(columns=COLUMNS,rows=get_rows(processor_data),row_key='name',title='Processor')

        with ui.row().classes('flex w-full'):
            processor_frequencies_data={
                'min':cpu_frequency.min,
                'max':cpu_frequency.max,
                'current':cpu_frequency.current,
            }
            processor_frequencies_table=ui.table(columns=COLUMNS,rows=get_rows(processor_frequencies_data),row_key='name',title='Frequencies (MHz)')

            processor_usage_data={
                f'Core {i}': usage
                for i,usage in enumerate(psutil.cpu_percent(percpu=True))
            }
            processor_usage_table=ui.table(columns=COLUMNS,rows=get_rows(processor_usage_data),row_key='name',title='Usage (%)').classes('flex-1')
    with ui.column():
        virtual_memory_data={
            'total':get_formatted_size(system_virtual_memory.total),
            'available':get_formatted_size(system_virtual_memory.available),
            'used':get_formatted_size(system_virtual_memory.used),
            'percentage':f'{system_virtual_memory.percent}%',
        }
        virtual_memory_table=ui.table(columns=COLUMNS,rows=get_rows(virtual_memory_data),row_key='name',title='Virtual Memory').classes('w-full')

        swap_memory_data={
            'total':get_formatted_size(swap.total),
            'free':get_formatted_size(swap.free),
            'used':get_formatted_size(swap.used),
            'percentage':f'{swap.percent}%',
        }
        swap_memory_table=ui.table(columns=COLUMNS,rows=get_rows(swap_memory_data),row_key='name',title='Swap Memory')
    with ui.column():
        with ui.card():
            ui.label('Disks').classes('q-table__title')
            disk_tables=defaultdict(dict)
            for partition in partitions:
                try: usage_data=psutil.disk_usage(partition.mountpoint)
                except: continue
                partition_name=win32api.GetVolumeInformation(partition.device)[0]
                disk_data={
                    'device':partition.device,
                    'name':partition_name,
                    'file system':partition.fstype,
                }
                space_data={
                    'total':get_formatted_size(usage_data.total),
                    'used':get_formatted_size(usage_data.used),
                    'free':get_formatted_size(usage_data.free),
                    'percentage':f'{usage_data.percent}%',
                }
                with ui.expansion(partition_name):
                    disk_tables[partition_name]['disk']=ui.table(columns=COLUMNS,rows=get_rows(disk_data),row_key='name',title=f'{partition_name} Data')
                    disk_tables[partition_name]['space']=ui.table(columns=COLUMNS,rows=get_rows(space_data),row_key='name',title=f'{partition_name} Space')
                    # TODO add some diagram showing how much space is available
            
            disks_data={
                'read':get_formatted_size(disk_io.read_bytes),
                'write':get_formatted_size(disk_io.write_bytes),
            }
            disks_table=ui.table(columns=COLUMNS,rows=get_rows(disks_data),row_key='name').classes('w-full')
    with ui.column():
        with ui.card():
            ui.label('Network').classes('q-table__title')
            network_tables=defaultdict(str)
            for interface_name,interface_addresses in if_addrs.items():
                interface_addresses=[a for a in interface_addresses if a.family.name=='AF_INET' or a.family.name=='AF_PACKET']
                for address in interface_addresses:
                    network_data={
                        'IP Address' if address.family.name=='AF_INET' else 'MAC Address':address.address,
                        'netmask':address.netmask,
                        'Broadcast IP' if address.family.name=='AF_INET' else 'Broadcast MAC':address.broadcast,
                    }
                    with ui.expansion(interface_name):
                        network_tables[interface_name]=ui.table(columns=COLUMNS,rows=get_rows(network_data),row_key='name',title=f'{interface_name} Data')
            network_data={
                'sent':get_formatted_size(net_io.bytes_sent),
                'received':get_formatted_size(net_io.bytes_recv),
            }
            network_table=ui.table(columns=COLUMNS,rows=get_rows(network_data),row_key='name').classes('w-full')
            # TODO add network usage plot
with ui.row():
    processor_usage_plot=ui.line_plot(n=1).with_legend(['CPU Usage %'],loc='upper center',ncol=1)
    processor_usage_plot.push([datetime.now().timestamp()],[[100]])



ui.timer(1,update_ui,active=True)
ui.run()
