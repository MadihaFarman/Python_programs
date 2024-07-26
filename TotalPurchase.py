item_1 = float(input('Enter price of first item: '))
item_2 = float(input('Enter price of second item: '))
item_3 = float(input('Enter price of third item: '))
item_4 = float(input('Enter price of fourth item: '))
item_5 = float(input('Enter price of fifth item: '))
subTotal = item_1 + item_2 + item_3 + item_4 + item_5
SALES_TAX = 0.07
total = (subTotal * SALES_TAX) + subTotal
print('Subtotal: ',subTotal)
print('Total bill after sales tax: ',total)