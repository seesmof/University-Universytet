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

import random
import nltk

while 1:
    HELP_MESSAGE='''Доступні команди:
- вийти АБО вихід: закриття програми
- поможи АБО допомога: виведення цього повідомлення
'''.strip()

    request=input('> ')
    request.lower()

    words=nltk.word_tokenize(request)
    print(words)

    if 'вихід' in words or 'вийти' in words: break
    elif 'поможи' in words or 'допомога' in words: print(HELP_MESSAGE)
    elif 'є' in words:
        all_clients_query=f'SELECT name FROM {CLIENTS_TABLE}'
        c.execute(all_clients_query)
        res=c.fetchall()
        print(','.join([r[0] for r in res]))