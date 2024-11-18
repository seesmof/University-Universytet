Вебдодаток керування фінансами, який забезпечує виконання одноразових та періодичних платежів клієнтами. Початкова кількість коштів на рахунку кожного клієнта та його кредитні ліміти визначаються менеджером, якому доступна вся інформаія про клієнтів. Клієнт може переглядати всю інформацію про власний рахунок (разом з історією транзакцій), вносити кошти, сплачувати за послуги, призначати періодичні платежі.

User 
  limit:int
  balance:int
  manager:bool
Pay
  periodic:bool
  amount:int
  purpose:str


- payment 
  - kind: single OR periodic 
  - amount: money 
  - date: date
  - user: user.id
- user 
  - name: str 
  - password: str (maybe) 
  - balance: money 
  - limit: money 
  - kind: client OR manager

- functions 
  - add money to balance 
  - see payments history 
  - make single payment 
  - make periodic payment
  - see user info if user.manager
  - set balance if user.manager
  - set limit if user.manager

'NAME':'data',
'USER':'root',
'HOST':'localhost',
'PASSWORD':'1313',
'DATABASE':'data',
'PORT':'3306',

A web-based financial management application that allows customers to make one-time and recurring payments. The initial amount of money on each client's account and credit limits are determined by the manager, who has access to all client information. The client can view all information about their account (including transaction history), deposit funds, pay for services, and schedule recurring payments.