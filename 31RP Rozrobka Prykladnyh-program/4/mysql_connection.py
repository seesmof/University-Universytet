NAME='data'
USER='root'
PASSWORD='1313'
HOST='localhost'
PORT='3306'

from peewee import *

db=MySQLDatabase(NAME,user=USER,password=PASSWORD,host=HOST,port=PORT)