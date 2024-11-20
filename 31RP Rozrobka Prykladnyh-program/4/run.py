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
- користувач: виведення даних про користувача
- баланс: виведення балансу користувача
- ліміт АБО кредит: виведення кредитного ліміту користувача
- менеджер АБО адміністратор: виведення статусу користувача
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
    
    def clean_query(
        query:list[str],
    ):
        return [
            word for word in query
            if 'буд' not in word
            and 'ласк' not in word
            and 'про' not in word
            and 'дан' not in word
            and 'інф' not in word
            and 'чи' not in word
        ]
    
    def show_clients(
    ):
        all_clients_query=f'SELECT name,balance,credit FROM {CLIENTS_TABLE}'
        c.execute(all_clients_query)
        rows=c.fetchall()
        for client in rows:
            name,balance,credit=client
            print(f'{name} має {balance} з {credit}')

    def get_user(
        user_name:str,
    ):
        client_query=f'SELECT name,balance,credit,manager FROM {CLIENTS_TABLE} WHERE name="{user_name}"'
        c.execute(client_query)
        rows=c.fetchall()[0]
        return rows
    
    def get_balance(
        user_name:str,
    ):
        client_query=f'SELECT name,balance FROM {CLIENTS_TABLE} WHERE name="{user_name}"'
        c.execute(client_query)
        r=c.fetchall()[0]
        return r

    def get_credit(
        user_name:str,
    ):
        client_query=f'SELECT name,credit FROM {CLIENTS_TABLE} WHERE name="{user_name}"'
        c.execute(client_query)
        r=c.fetchall()[0]
        return r
    
    def get_manager(
        user_name:str,
    ):
        client_query=f'SELECT name,manager FROM {CLIENTS_TABLE} WHERE name="{user_name}"'
        c.execute(client_query)
        r=c.fetchall()[0]
        return r
    
    if check_any(['вих','вий']): break
    elif check_any(['пом','доп']): print(HELP_MESSAGE)
    elif check_any(['користувачі']): show_clients()
    elif check_any(['баланс']):
        stripped_words=clean_query([w for w in words if 'балан' not in w])
        found=False
        for word in stripped_words:
            try:
                name,balance=get_balance(word)
                print(f'{name} має {balance} на рахунку')
                found=True
                break
            except:
                continue
        if not found: print('користувача не знайдено')
    elif check_any(['кредит','ліміт']):
        stripped_words=clean_query([w for w in words if 'балан' not in w])
        found=False
        for word in stripped_words:
            try:
                name,balance=get_credit(word)
                print(f'{name} має {balance} кредитного ліміту')
                found=True
                break
            except:
                continue
        if not found: print('користувача не знайдено')
    elif check_any(['мен','адм']):
        stripped_words=clean_query([w for w in words if 'мен' not in w and 'адм' not in w])
        found=False
        for word in stripped_words:
            try:
                name,manager=get_manager(word)
                print(f'{name} {"є" if manager else "не є"} менеджером')
                found=True
                break
            except:
                continue
        if not found: print('користувача не знайдено')
    elif check_any(['користувач']):
        stripped_words=clean_query([w for w in words if 'користувач' not in w])
        found=False
        for word in stripped_words:
            try:
                name,balance,credit,is_manager=get_user(word)
                print(f'{name} має {balance} на рахунку, {credit} кредитного ліміту, та {"є" if is_manager else "не є"} менеджером')
                found=True
                break
            except:
                continue
        if not found: print('користувача не знайдено')