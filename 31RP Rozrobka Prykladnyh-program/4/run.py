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
- користувачі: виведення списку користувачів
'''.strip()

    request=input('> ')
    words=nltk.word_tokenize(request.lower())

    def check_any(
        terms:list[str],
        words:list[str]=words,
    ):
        found=False
        for term in terms:
            for word in words:
                if term in word:
                    found=True
                    break
        return found
    
    def check_all(
        terms:list[str],
        words:list[str]=words,
    ):
        all_good=True
        for term in terms:
            found=False
            for word in words:
                if term in word: found=True
            if not found:
                all_good=False
                break
        return all_good

    if check_any(['вихід','вийти']): break
    elif check_any(['поможи','допомога']): print(HELP_MESSAGE)
    elif check_all(['є','користувач']):

    elif 'є' in words:
        all_clients_query=f'SELECT name FROM {CLIENTS_TABLE}'
        c.execute(all_clients_query)
        res=c.fetchall()
        print(','.join([r[0] for r in res]))