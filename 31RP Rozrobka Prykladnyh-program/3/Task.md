Вебдодаток керування фінансами, який забезпечує виконання одноразових та періодичних платежів клієнтами. Початкова кількість коштів на рахунку кожного клієнта та його кредитні ліміти визначаються менеджером, якому доступна вся інформаія про клієнтів. Клієнт може переглядати всю інформацію про власний рахунок (разом з історією транзакцій), вносити кошти, сплачувати за послуги, призначати періодичні платежі.

Pay
  periodic:bool
  amount:int
  purpose:str
User 
  balance:int
  limit:int
  manager:bool


- payment 
  - kind: single OR periodic 
  - amount: money 
  - date: date
  - user: user.id

- functions 
  - add money to balance 
  - see payments history 
  - make single payment 
  - make periodic payment
  - see user info if user.manager
  - set balance if user.manager
  - set limit if user.manager

'USER': 'root',
'PASSWORD': '1313',
'HOST': 'localhost',
'PORT': '3306',
'NAME': 'data',
