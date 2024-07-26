food_charge = float(input('Enter charge for food: '))
tip = 0.18
sales_tax = 0.07
amount_after_tip = (food_charge * tip) + food_charge
amount_after_salesTax = (food_charge * sales_tax) + food_charge
totalAmount = (food_charge*(tip + sales_tax)) + food_charge
print("Amount after tip:",amount_after_tip)
print('Amount after sales tax:',amount_after_salesTax)
print('Total amount:',totalAmount)