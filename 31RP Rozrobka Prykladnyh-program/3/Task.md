# Task Description
Вебдодаток керування фінансами, який забезпечує виконання одноразових та періодичних платежів клієнтами. Початкова кількість коштів на рахунку кожного клієнта та його кредитні ліміти визначаються менеджером, якому доступна вся інформація про клієнтів. Клієнт може переглядати всю інформацію про власний рахунок (разом з історією транзакцій), вносити кошти, сплачувати за послуги, призначати періодичні платежі.

# List of Functions
- [x] add money to balance (take away from credit and add to balance)
- [x] see all users info IF user.manager 
- [x] change balance IF user.manager 
- [x] change limit IF user.manager 
- [ ] see payments history 
- [ ] make single payment 
- [ ] make periodic payment 

# MySQL Database Setup
'USER': 'root',
'PASSWORD': '1313',
'HOST': 'localhost',
'PORT': '3306',
'NAME': 'data',

# Models Architecture
User 
  name = str 
  balance = int 
  credit = int 
Transaction 
  user = user id 
  amount = int 