import psutil
import time

UPDATE_DELAY = 1 # in seconds

def get_formatted_size(bytes):
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024: return f"{bytes:.2f} {unit}B"
        bytes /= 1024

io=psutil.net_io_counters()
sent,recv=io.bytes_sent,io.bytes_recv
while 1:
    time.sleep(UPDATE_DELAY)
    new_io=psutil.net_io_counters()
    us,ds=new_io.bytes_sent-sent,new_io.bytes_recv-recv
    print('upload',get_formatted_size(new_io.bytes_sent))
    print('download',get_formatted_size(new_io.bytes_recv))
    print('upload speed',get_formatted_size(us/UPDATE_DELAY))
    print('download speed',get_formatted_size(ds/UPDATE_DELAY))
    sent,recv=new_io.bytes_sent,new_io.bytes_recv