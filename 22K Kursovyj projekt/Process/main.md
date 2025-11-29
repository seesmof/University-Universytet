for esc key macro to work:

- set key preview of form to true
- write this in On Key Press event code builder:

```
  If KeyAscii = 27 Then
    DoCmd.RunMacro "Close_Payroll_Form_Macro"
  End If
```

in payroll we need to have:

- Employee_ID
- Monthly_Salary
- Total_Tax_Rate
- Total_Tax
- Bonuses
- Deductions
- Net_Pay

add menu

look into tables and make sure all good there