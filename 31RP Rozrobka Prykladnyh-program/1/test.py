from pprint import pprint
from new import *

m=Movie("ISUSE SPASY")
m.generate_rooms()
for r in m.rooms: pprint(r.number)
d=DataProcessor()
pprint(d.get_path("data.json"))