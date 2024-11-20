NAME='data'
USER='root'
PASSWORD='1313'
HOST='localhost'
PORT='3306'

import mysql.connector

db=mysql.connector.connect(database=NAME,user=USER,password=PASSWORD,host=HOST,port=PORT)
c=db.cursor()

CLIENTS_TABLE='finance_client'
PAYMENTS_TABLE='finance_payment'
PERIODIC_PAYMENTS_TABLE='finance_periodicpayment'

c.execute(f'SELECT * FROM {CLIENTS_TABLE}')
r=c.fetchall()
print(r)

import random

while 1:
    HELP_MESSAGE='''Доступні команди:
- вийти АБО вихід: закриття програми
- поможи АБО допомога: виведення цього повідомлення
'''.strip()

    request=input('> ')
    request.lower()

    if 'вихід' in request or 'вийти' in request: break
    elif 'поможи' in request or 'допомога' in request: print(HELP_MESSAGE)
    elif 'привіт' in request or 'вітаю' in request: print(request)
    elif 'як справи' in request: print(random.choice(['нормально','добре','чудово']))