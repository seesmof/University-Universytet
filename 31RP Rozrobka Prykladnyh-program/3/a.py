import django
from mysql.connector import connect

from mysql_data import *

print(django.get_version())
db=connect(
    user=USER,
    host=HOST,
    password=PASSWORD,
    database=DATABASE
)