
# celsius_1 = float(input('temperature value in degree Celsius:'))

# Fahrenheit_1 = (celsius_1 * 1.8) +32

# print('The %.2f degree Celsius is equal to: %.2totalf Fahrenheit' %(celsius_1, Fahrenheit_1))

# print('----OR----')
# celsius_2 = float(input('Temperature value in degree Celsius:'))
# Fahrenheit_2 = (celsius_2 * 9/5) + 35

# print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'  
#       %(celsius_2, Fahrenheit_2))

work_hours = float(input('Enter Hours:'))
pay_rate = float(input('Enter Rate:'))

if work_hours <= 40:
  pay = work_hours * pay_rate
else:
  pay = ((work_hours - 40) * (1.5 * pay_rate)) + (40 * pay_rate)

print (f'Total pay is {pay}!')