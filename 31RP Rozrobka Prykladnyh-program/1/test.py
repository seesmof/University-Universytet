from run import DataHandler
filer=DataHandler("data")
d=filer.read_data()
print(d.keys())