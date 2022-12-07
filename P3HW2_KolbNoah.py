#CTI-110
#P3HW2-Salary
#Noah Kolb
#10/26/22
#
print("Enter employee's name: ", end='')
employeeName = str(input())
print('Enter number of hours worked: ', end='')
hoursWorked = float(input())
print("Enter employee's pay rate: ", end='')
payRate = float(input())
overTime = (hoursWorked-40)
if overTime < 1:
    overTime = 0
overPay = (overTime*(payRate*1.5))
regPay = (hoursWorked - overTime)*payRate
grossPay = overPay+regPay
print('---------------------------')
print('Employee name:  ', employeeName)
print('')
print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('--------------------------------------------------------------------------------')
print(hoursWorked, end='           ')
print(payRate, end='       ')
print(overTime, end='        ')
print(overPay, end='          ')
print(regPay, end='          ')
print(grossPay)
