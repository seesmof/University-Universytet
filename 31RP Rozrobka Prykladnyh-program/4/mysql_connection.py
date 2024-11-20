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

CLIENTS_TABLE='finance_client'
PAYMENTS_TABLE='finance_payment'
PERIODIC_PAYMENTS_TABLE='finance_periodicpayment'

c.execute(f'SELECT * FROM {CLIENTS_TABLE}')
r=c.fetchall()
print(r)

c.execute(f'SHOW COLUMNS FROM {CLIENTS_TABLE}')
r=c.fetchall()
print(r)