<div align="center">
  <h1>Курсовий Проєкт</h1>
  <h3>Автоматизована система розрахунку заробітної плати</h3>
  <p>Виконано Онищенко Олегом, студентом групи КНТ-122</p>
</div>

### Резюме

База даних призначена для розрахунку заробітної плати працівників фірми

Система передбачає автоматичний розрахунок заробітної плати працівників фірми з урахуванням податків

### Схема даних

![](https://i.imgur.com/QHFaRne.png)

### Таблиці

#### Bonuses Table

##### Preview

![](https://i.imgur.com/QSJwckV.png)

##### Designer

![](https://i.imgur.com/OHB5Kim.png)

#### Deductions Table

##### Preview

![](https://i.imgur.com/PBTMhQ6.png)

##### Designer

![](https://i.imgur.com/3MdOkBb.png)

#### Department Table

##### Preview

![](https://i.imgur.com/tTJnaEi.png)

##### Designer

![](https://i.imgur.com/qUHeOOM.png)

#### Employee Table

##### Preview

![](https://i.imgur.com/qtVVwEt.png)

##### Designer

![](https://i.imgur.com/YQd6aIK.png)

#### Payroll Table

##### Preview

![](https://i.imgur.com/1twO5w4.png)

##### Designer

![](https://i.imgur.com/0XcImw6.png)

#### Position Table

##### Preview

![](https://i.imgur.com/AXic79r.png)

##### Designer

![](https://i.imgur.com/umKekoP.png)

#### Tax Rate Table

##### Preview

![](https://i.imgur.com/q9S0SLd.png)

##### Designer

![](https://i.imgur.com/3bfTjC9.png)

### Запити

#### New Payroll Record Query

##### Designer

![](https://i.imgur.com/GDAkId6.png)

##### SQL

```SQL
INSERT INTO Payroll_Table (
  Employee_ID,
  Monthly_Salary,
  Total_Tax_Rate,
  Total_Tax,
  Bonuses,
  Deductions,
  Net_Pay,
  [Current_Date]
)
SELECT [Forms]![Employee_Form]![Employee_ID] AS Expr1,
  [Forms]![Employee_Form]![Monthly_Salary_Input] AS Expr2,
  [Forms]![Employee_Form]![Total_Tax_Rate_Input] AS Expr3,
  [Forms]![Employee_Form]![Total_Tax_Input] AS Expr4,
  [Forms]![Employee_Form]![Total_Bonuses_Input] AS Expr5,
  [Forms]![Employee_Form]![Total_Deductions_Input] AS Expr6,
  [Forms]![Employee_Form]![Net_Income_Input] AS Expr7,
  Date() AS Expr8;
```

#### Employee Data Query

##### Designer

![](https://i.imgur.com/TQ9AXfY.png)

##### SQL

```SQL
SELECT Employee_Table.Employee_ID,
  Employee_Table.Employee_Name,
  Position_Table.Position_Name,
  Position_Table.Position_Monthly_Salary,
  Department_Table.Department_Name,
  Employee_Table.Employee_Gender
FROM (Department_Table
  INNER JOIN Position_Table
    ON Department_Table.Department_ID = Position_Table.Position_Department)
  INNER JOIN Employee_Table
    ON Position_Table.Position_ID = Employee_Table.Employee_Position
WHERE (Employee_Table.Employee_ID) = [Forms]![Employee_Form]![Employee_ID_Input];
```

#### Total Tax Rate Query

##### Designer

![](https://i.imgur.com/vVbicMG.png)

##### SQL

```SQL
SELECT Sum([Tax_Rate]) AS Total_Tax_Rate
FROM Tax_Rate_Table;
```

### Форми

#### Bonuses Form

##### Preview

![](https://i.imgur.com/lNw15OX.png)

##### Designer

![](https://i.imgur.com/amq5B6f.png)

#### Deductions Form

##### Preview

![](https://i.imgur.com/lvRNPr1.png)

##### Designer

![](https://i.imgur.com/UY9zCeO.png)

#### Employee Data Form

##### Preview

![](https://i.imgur.com/litNkhi.png)

##### Designer

![](https://i.imgur.com/on3TrKR.png)

#### Employee Form

##### Preview

![](https://i.imgur.com/9aSU633.png)

##### Designer

![](https://i.imgur.com/G4dVxWi.png)

#### Menu Form

##### Preview

![](https://i.imgur.com/7zOG7wM.png)

##### Designer

![](https://i.imgur.com/7t6mWx6.png)

#### Payroll Form

##### Preview

![](https://i.imgur.com/AZZQYzj.png)

##### Designer

![](https://i.imgur.com/qSK25AL.png)

#### Tax Rate Form

##### Preview

![](https://i.imgur.com/4FFg9HO.png)

##### Designer

![](https://i.imgur.com/YkrIY5S.png)

### Звіти

#### Employee Data Report

##### Preview

![](https://i.imgur.com/Y6HbQEN.png)

##### Designer

![](https://i.imgur.com/r8orAsq.png)

#### Payroll Report

##### Preview

![](https://i.imgur.com/MRV9l9a.png)

##### Designer

![](https://i.imgur.com/ZYAQ0so.png)

#### Tax Rate Report

##### Preview

![](https://i.imgur.com/GYQc6BG.png)

##### Designer

![](https://i.imgur.com/VCvp1Na.png)

### Макроси

#### Close Employee Form Macro

![](https://i.imgur.com/EIcIPmQ.png)

#### Close Payroll Form Macro

![](https://i.imgur.com/rm499mx.png)

#### Close Payroll Report Macro

![](https://i.imgur.com/PVJfIck.png)