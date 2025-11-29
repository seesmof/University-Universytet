import psutil as ps
import subprocess as sp
import wmi

BYTES_TO_GB=10**9

computer=wmi.WMI()
cpu=computer.Win32_Processor()[0]
gpu=computer.Win32_VideoController()[0]
print(gpu)

print('RAM Total Size',f'{ps.virtual_memory().total/BYTES_TO_GB:.1f}')
print('RAM Used Size',f'{ps.virtual_memory().used/BYTES_TO_GB:.1f}')
print('RAM Speed',)

print('Storage Device Name',)
print('Storage Device Total Space',)
print('Storage Device Available Space',)

print('CPU Name',)
print('CPU Cores',)
print('CPU Load Percentage',)

print('GPU Name',gpu.VideoProcessor)
print('GPU Memory Size',)
print('GPU Load Percentage',)

def get_gpu_memory():
    command = "nvidia-smi --query-gpu=memory.free --format=csv"
    memory_free_info = sp.check_output(command.split()).decode('ascii').split('\n')[:-1][1:]
    memory_free_values = [int(x.split()[0]) for i, x in enumerate(memory_free_info)]
    return memory_free_values

print(get_gpu_memory())
