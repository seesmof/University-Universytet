Payroll_Table
Payroll_ID int primary key auto
Employee_ID int foreign key references Employee_Table(Employee_ID)
Monthly_Salary money
Total_Tax_Rate float
Total_Tax money
Bonuses money
Deductions money
Net_Pay money
Current_Date date default Date()

Tax_Rate_Table
Tax_ID int primary key auto
Tax_Type varchar(255)
Tax_Rate float

Employee_Table
Employee_ID int primary key auto
Employee_Name varchar(255)
Employee_Position int foreign key references Position_Table(Position_ID)
Employee_Gender varchar(7) select("Male", "Female")

Deductions_Table
Deduction_ID int primary key auto
Employee_ID int foreign key references Employee_Table(Employee_ID)
Deduction_Amount money

Bonuses_Table
Bonus_ID int primary key auto
Employee_ID int foreign key references Employee_Table(Employee_ID)
Bonus_Amount money

Postion_Table
Position_ID int primary key auto
Position_Name varchar(255)
Position_Department int foreign key references Department_Table(Department_ID)
Position_Monthly_Salary money

Department_Table
Department_ID int primary key auto
Department_Name varchar(255)