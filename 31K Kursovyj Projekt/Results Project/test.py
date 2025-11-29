import psutil

print(psutil.cpu_percent(percpu=True))
print(psutil.cpu_percent())