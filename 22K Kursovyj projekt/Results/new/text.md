**Міністерство Освіти і Науки України**
_Національний університет «Запорізька політехніка»_

Факультет Комп’ютерних наук і технологій
Кафедра Програмних засобів
Спеціальність 121 «Інженерія програмного забезпечення»

**Завдання на курсовий проєкт**

1. Тема курсової роботи – Автоматизована система розрахунку заробітної плати
2. Строк подання студентом роботи – до 23.05.2024
3. Вихідні дані по роботі – технічне завдання
4. Зміст пояснювальної записки – резюме, інформаційна компонента системи, компонента автоматизації системи

Дата видачі завдання 23 березня 2024 року

#### Резюме

База даних призначена для обліку заробітних плат працівників фірми. База даних містить додаткові засоби обліку бонусів та відрахувань працівників, а також засоби обчислення та взаємодії з наявними податковими ставками на заробітну плату.

База даних включає такі таблиці: Bonuses, Deductions, Department, Employee, Payroll, Position, Tax Rate

Перелік функцій Бази Даних: система має створювати особисту сторінку для кожного працівника. На такій сторінці має бути перелічена вся особиста інформація про працівника. Нижче від особистої інформації людини мають бути перелічені всі її поточні бонуси та відрахування, а також інформація про наявні звіти заробітної плати. У тій же секції має бути передбачена інформація про поточні податкові ставки на заробітну плату. Головна секція такої сторінки має здійснювати автоматичні підрахунки заробітної плати працівника з можливістю додати відповідний запис у таблицю заробітніх плат.

#### Інформаційна компонента системи

##### Опис таблиць та зв'язків

| Назва          | Клас         | Ступінь | Ключ                | Зв'язана                       |
| -------------- | ------------ | ------- | ------------------- | ------------------------------ |
| Employee_Table | Обов'язковий | 1:N     | Employee_ID         | Payroll_Table.Employee_ID      |
| Employee_Table | Обов'язковий | 1:N     | Employee_ID         | Deductions_Table.Employee_ID   |
| Employee_Table | Обов'язковий | 1:N     | Employee_ID         | Bonuses_Table.Employee_ID      |
| Employee_Table | Обов'язковий | N:1     | Employee_Position   | Position_Table.Position_ID     |
| Position_Table | Обов'язковий | N:1     | Position_Department | Department_Table.Department_ID |

##### Опис атрибутів

| Назва                   | Ключ?   | Тип     | Обов'язковий |
| ----------------------- | ------- | ------- | ------------ |
| _Payroll_Table_         |
| Payroll_ID              | primary | int     | +            |
| Employee_ID             | foreign | int     | +            |
| Monthly_Salary          | -       | money   | +            |
| Total_Tax_Rate          | -       | float   | +            |
| Total_Tax               | -       | money   | +            |
| Bonuses                 | -       | money   | -            |
| Deductions              | -       | money   | -            |
| Net_Pay                 | -       | money   | +            |
| Current_Date            | -       | date    | +            |
| _Tax_Rate_Table_        |
| Tax_ID                  | primary | int     | +            |
| Tax_Type                | -       | varchar | +            |
| Tax_Rate                | -       | float   | +            |
| _Employee_Table_        |
| Employee_ID             | primary | int     | +            |
| Employee_Name           | -       | varchar | +            |
| Employee_Position       | -       | int     | +            |
| Employee_Gender         | -       | varchar | -            |
| _Deductions_Table_      |
| Deduction_ID            | primary | int     | +            |
| Employee_ID             | foreign | int     | +            |
| Deduction_Amount        | -       | money   | +            |
| _Bonuses_Table_         |
| Bonus_ID                | primary | int     | +            |
| Employee_ID             | foreign | int     | +            |
| Bonus_Amount            | -       | money   | +            |
| _Postion_Table_         |
| Position_ID             | primary | int     | +            |
| Position_Name           | -       | varchar | +            |
| Position_Department     | foreign | int     | +            |
| Position_Monthly_Salary | -       | money   | +            |
| _Department_Table_      |
| Department_ID           | primary | int     | +            |
| Department_Name         | -       | varchar | +            |

##### Схема даних

![image.png](https://photos.app.goo.gl/h8bBmeJtHjd1kEJVA)

#### Компонента автоматизації системи
##### Запити 

- New_Payroll_Record_Query - додає новий запис у таблицю заробітніх плат
- Employee_Data_Query - повертає всю необхнідну облікову інформацію про працівника
- Total_Tax_Rate_Query - повертає загальну податкову ставку як суму всіх навяних податкових ставок

|Назва|Тип|Вхід|Обчислення|Використання|
|-|-|-|-|-|
|New_Payroll_Record_Query|append|Employee_ID, Monthly_Salary, Total_Tax_Rate, Total_Tax, Bonuses, Deductions, Net_Pay, Current_Date|Current_Date = Date()|Employee_Form|
|Employee_Data_Query|select|Employee_ID|-|Employee_Form|
|Total_Tax_Rate_Query|select|Tax_Rate_Table.Tax_Rate|Sum(Tax_Rate_Table.Tax_Rate)|Employee_Form|

##### Звіти

- Employee_Data_Report - підзвіт для перегляду даних про працівника
- Payroll_Report - звіт по заробітній платі за конкретний місяць
- Tax_Rate_Report - звіт за всіма навяними податковими ставками

|Назва|Дані|Використання|
|-|-|-|
|Employee_Data_Report|Employee_ID, Employee_Name, Employee_Position, Monthly_Salary, Department_Name, Gender|Payroll_Report|
|Payroll_Report|всі поля з Employee_Data_Report|Employee_Form|
|Tax_Rate_Report|Tax_Type, Tax_Rate|Employee_Form|

##### Макроси

- Close_Employee_Form_Macro - закриває форму працівника
- Close_Payroll_Form_Macro - закриває форму заробітної плати
- Close_Payroll_Report_Macro - закриває звіт по заробітній платі

|Назва|Використання|
|-|-|
|Close_Employee_Form_Macro|Employee_Form|
|Close_Payroll_Form_Macro|Payroll_Form|
|Close_Payroll_Report_Macro|Payroll_Report|