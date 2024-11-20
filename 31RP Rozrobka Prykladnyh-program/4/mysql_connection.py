NAME='data'
USER='root'
PASSWORD='1313'
HOST='localhost'
PORT='3306'

from peewee import *

db=MySQLDatabase(NAME,user=USER,password=PASSWORD,host=HOST,port=PORT)

import mysql.connector

db=mysql.connector.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=PORT)
c=db.cursor()
c.execute('SELECT table FROM tables')
r=c.fetchall()
print(r)