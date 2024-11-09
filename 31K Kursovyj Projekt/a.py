import psutil as ps

BYTES_TO_GB=10**9

print('RAM Total Size',f'{ps.virtual_memory().total/BYTES_TO_GB:.1f}')
print('RAM Used Size',f'{ps.virtual_memory().used/BYTES_TO_GB:.1f}')
print('RAM Speed',)

print('Storage Device Name',)
print('Storage Device Total Space',)
print('Storage Device Available Space',)

print('CPU Name',)
print('CPU Cores',)
print('CPU Load Percentage',)

print('GPU Name',)
print('GPU Memory Size',)
print('GPU Load Percentage',)