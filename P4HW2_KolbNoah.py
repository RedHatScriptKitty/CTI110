# CTI-110
# P4HW2 - Salary Calculator
# Kolb Noah
# 11/16/22
#
emplEntr = 0
ttlOvr = 0.0
ttlHrs = 0.0
ttlGrs = 0.0
end = "false"
while end == "false":
    print("Enter employee's name or"' "None"'" to terminate" ,end=' ')
    name = str(input())
    name = name.capitalize()
    if name == "None":
        print (f'Total number of employees entered :{emplEntr}')
        print (f'Total amount payed for overtime:',"%.2f" % ttlOvr)
        print (f'Total amount payed for regular hours:',"%.2f" %  ttlHrs)
        print (f'Total amount payed in gross:',"%.2f" %  ttlGrs)
        end = "true"
        
    else:
        emplEntr = emplEntr + 1
        print(f'How many hours did {name} worked?',end=' ')
        hoursWorked = float(input())
        print(f'What is {name} pay rate?',end=' ')
        payRate = float(input())
        
        overTime = (hoursWorked-40)
        if overTime < 1:
            overTime = 0
        overPay = (overTime*(payRate*1.5))
        regPay = (hoursWorked - overTime)*payRate
        grossPay = overPay+regPay
        

        ttlOvr = ttlOvr + overPay
        ttlHrs = ttlHrs + regPay
        ttlGrs = ttlGrs +grossPay
            
        print('Employee name:  ', name)
        print('')
        print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
        print('--------------------------------------------------------------------------------')
        print("%.1f" %hoursWorked, end='           ')
        print("%.1f" %payRate, end='       ')
        print("%.1f" %overTime, end='        ')
        print("%.2f" %overPay, end='          ')
        print("%.2f" %regPay, end='          ')
        print("%.2f" %grossPay)
        print()
