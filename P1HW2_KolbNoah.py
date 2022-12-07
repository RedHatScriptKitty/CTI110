# this program dislays and caclulates travel exenses
# 9/26/22
# CTI-110 P1HW2 - Travel Expense
# Noah Kolb
#
print('Enter budget:', end=' ')
budget = float(input())
print(' ')
print('Where is your traverl destination?', end=' ')
destination = input()
print(' ')
print('Enter the estimated ammount that will be spent on gas:', end=' ')
gas = float(input())
print(' ')
print('Enter the estimated ammount that will be spent on accomodations:', end=' ')
accomodations = float(input())
print(' ')
print('Enter the estimated ammount that will be spent on food:', end=' ')
food = float(input())
print(' ')
cost = gas+food+accomodations
remain = budget-cost
print('--------------Travel Exenses--------------')
print('location:', destination)
print('Initial Budget:', budget)
print(' ')
print('Fuel:', gas)
print('Accomodation:', accomodations)
print('Food:', food)
print(' ')
print('Total Exenses', cost)
print('Remaining Ballance:', remain)
      
