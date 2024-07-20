#get future desired amount
future_value = float(input('Enter desired future value: '))
#get annual interest rate
rate = float(input('Enter annual interest rate: '))
#get the number of years
years = int(input('Enter the number of years: '))
#calculate the amount to be deposited
present_amount = future_value / (1.0 + rate)**years
#display present amount
print('You will need to deposit this amount: ',present_amount)
result = 9 / 2
print('result is : ',result)