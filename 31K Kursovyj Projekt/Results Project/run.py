from collections import defaultdict
from datetime import datetime
from nicegui import ui
import win32api
import platform
import psutil

CENTER_CLASSES='-center w-full'
COLUMNS=[
    {'name':'property','label':'Property','field':'property','align':'left'},
    {'name':'value','label':'Value','field':'value','sortable':True},
]

system=platform.uname()
boot_time=datetime.fromtimestamp(psutil.boot_time())
cpu_frequencies=psutil.cpu_freq()
virtual_memory=psutil.virtual_memory()
swap_memory=psutil.swap_memory()
partitions=psutil.disk_partitions()
disks=psutil.disk_io_counters()
networks=psutil.net_if_addrs()
network=psutil.net_io_counters()
network_sent,network_received=network.bytes_sent,network.bytes_recv

def get_rows(data:dict):
    return [{'property':k.capitalize(),'value':v} for k,v in data.items()]

def update_ui():
    processor_frequencies_data={
        'min':cpu_frequencies.min,
        'max':cpu_frequencies.max,
        'current':cpu_frequencies.current,
    }
    processor_frequencies_table.rows=get_rows(processor_frequencies_data)

    cpu_usage=psutil.cpu_percent(percpu=True)
    processor_usage_data={
        f'Core {i}': usage
        for i,usage in enumerate(cpu_usage)
    }
    processor_usage_table.rows=get_rows(processor_usage_data)

    cpu_usage=psutil.cpu_percent()
    this_time=datetime.now().timestamp()
    processor_usage_plot.push([this_time],[[cpu_usage]])

    system_virtual_memory=psutil.virtual_memory()
    virtual_memory_data={
        'total':get_formatted_size(system_virtual_memory.total),
        'available':get_formatted_size(system_virtual_memory.available),
        'used':get_formatted_size(system_virtual_memory.used),
        'percentage':f'{system_virtual_memory.percent}%',
    }
    virtual_memory_table.rows=get_rows(virtual_memory_data)
    virtual_memory_circle.value=system_virtual_memory.percent
    memory_usage_plot.push([this_time],[[system_virtual_memory.percent]])

    swap=psutil.swap_memory()
    swap_memory_data={
        'total':get_formatted_size(swap.total),
        'free':get_formatted_size(swap.free),
        'used':get_formatted_size(swap.used),
        'percentage':f'{swap.percent}%',
    }
    swap_memory_table.rows=get_rows(swap_memory_data)
    swap_memory_circle.value=swap.percent

    global network_sent,network_received
    new_network_io=psutil.net_io_counters()
    us,ds=new_network_io.bytes_sent-network_sent,new_network_io.bytes_recv-network_received
    BITS_TO_KILOBITS=10**-3
    download_speed,upload_speed=ds/1*BITS_TO_KILOBITS,us/1*BITS_TO_KILOBITS
    network_speed_plot.push([this_time],[[download_speed],[upload_speed]])
    network_sent,network_received=new_network_io.bytes_sent,new_network_io.bytes_recv

def get_formatted_size(bytes,suffix='B'):
    factor=1024
    for unit in ['','K','M','G','T','P']:
        if bytes<factor: return f'{bytes:.2f} {unit}{suffix}'
        bytes/=factor

with ui.row().classes('flex gap-3'):
    with ui.column():
        system_data={
            'type':system.system,
            'user':system.node,
            'release':system.release,
            'version':system.version,
            'machine':system.machine,
            'booted':f'{boot_time.day}.{boot_time.month}.{boot_time.year} {boot_time.hour:02d}:{boot_time.minute:02d}:{boot_time.second:02d}'
        }
        system_table=ui.table(columns=COLUMNS,rows=get_rows(system_data),row_key='name',title='System')
    with ui.column():
        processor_data={
            'name':system.processor,
            'platform':system.machine,
            'cores':psutil.cpu_count(logical=False),
            'threads':psutil.cpu_count(logical=True),
        }
        processor_table=ui.table(columns=COLUMNS,rows=get_rows(processor_data),row_key='name',title='Processor')

        with ui.row().classes('flex w-full'):
            with ui.column():
                processor_frequencies_data={
                    'min':cpu_frequencies.min,
                    'max':cpu_frequencies.max,
                    'current':cpu_frequencies.current,
                }
                processor_frequencies_table=ui.table(columns=COLUMNS,rows=get_rows(processor_frequencies_data),row_key='name',title='Frequencies (MHz)')

                ui.label('Processor Frequency').classes('text'+CENTER_CLASSES)
                processor_frequencies_circle=ui.circular_progress(min=cpu_frequencies.min,max=cpu_frequencies.max,value=cpu_frequencies.current).classes('self'+CENTER_CLASSES)

            processor_usage_data={
                f'Core {i}': usage
                for i,usage in enumerate(psutil.cpu_percent(percpu=True))
            }
            processor_usage_table=ui.table(columns=COLUMNS,rows=get_rows(processor_usage_data),row_key='name',title='Usage (%)').classes('flex-1')
    with ui.column():
        virtual_memory_data={
            'total':get_formatted_size(virtual_memory.total),
            'available':get_formatted_size(virtual_memory.available),
            'used':get_formatted_size(virtual_memory.used),
            'percentage':f'{virtual_memory.percent}%',
        }
        virtual_memory_table=ui.table(columns=COLUMNS,rows=get_rows(virtual_memory_data),row_key='name',title='Virtual Memory').classes('w-full')

        ui.label('Virtual Memory Usage').classes('text'+CENTER_CLASSES)
        virtual_memory_circle=ui.circular_progress(value=virtual_memory.percent,max=100).classes('self'+CENTER_CLASSES)

        swap_memory_data={
            'total':get_formatted_size(swap_memory.total),
            'free':get_formatted_size(swap_memory.free),
            'used':get_formatted_size(swap_memory.used),
            'percentage':f'{swap_memory.percent}%',
        }
        swap_memory_table=ui.table(columns=COLUMNS,rows=get_rows(swap_memory_data),row_key='name',title='Swap Memory')

        ui.label('Swap Memory Usage').classes('text'+CENTER_CLASSES)
        swap_memory_circle=ui.circular_progress(value=swap_memory.percent,max=100).classes('self'+CENTER_CLASSES)
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
                    disk_tables[partition_name]['disk']=ui.table(columns=COLUMNS,rows=get_rows(disk_data),row_key='name',title=f'{partition_name} Data').classes('w-full')
                    disk_tables[partition_name]['space']=ui.table(columns=COLUMNS,rows=get_rows(space_data),row_key='name',title=f'{partition_name} Space').classes('w-full')

                    ui.label(f'{partition_name} Usage').classes('text'+CENTER_CLASSES)
                    ui.circular_progress(value=usage_data.percent,max=100,min=0).classes('self'+CENTER_CLASSES)
            
            disks_data={
                'read':get_formatted_size(disks.read_bytes),
                'write':get_formatted_size(disks.write_bytes),
            }
            disks_table=ui.table(columns=COLUMNS,rows=get_rows(disks_data),row_key='name').classes('w-full')
    with ui.column():
        with ui.card():
            ui.label('Network').classes('q-table__title')
            network_tables=defaultdict(str)
            for interface_name,interface_addresses in networks.items():
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
                'sent':get_formatted_size(network.bytes_sent),
                'received':get_formatted_size(network.bytes_recv),
            }
            network_table=ui.table(columns=COLUMNS,rows=get_rows(network_data),row_key='name').classes('w-full')
with ui.row():
    processor_usage_plot=ui.line_plot(n=1,figsize=(4.7,2.47)).with_legend(['CPU Usage %'],loc='upper center',ncol=1)
    processor_usage_plot.push([datetime.now().timestamp()],[[0]])
    processor_usage_plot.push([datetime.now().timestamp()],[[100]])

    memory_usage_plot=ui.line_plot(n=1,figsize=(4.7,2.47)).with_legend(['RAM Usage %'],loc='upper center',ncol=1)
    memory_usage_plot.push([datetime.now().timestamp()],[[0]])
    memory_usage_plot.push([datetime.now().timestamp()],[[100]])

    network_speed_plot=ui.line_plot(n=2,figsize=(4.7,2.47)).with_legend(['Download Speed','Upload Speed'],loc='upper center',ncol=2)
    network_speed_plot.push([datetime.now().timestamp()],[[0],[0]])
    network_speed_plot.push([datetime.now().timestamp()],[[100],[100]])

ui.timer(1,update_ui,active=True)
ui.run(title='System Resources Analysis',favicon='💻')
