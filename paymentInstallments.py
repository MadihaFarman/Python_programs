amountOfPurchase = float(input('Enter amount of purchase:'))
numOfInstallments = float(input('Enter number of installments:'))
PERCENT = 0.05
totalAmount = (PERCENT * amountOfPurchase) + amountOfPurchase
print('Total purchase amount:',totalAmount)
costPerInstallment = totalAmount /numOfInstallments
print('Cost per installment is:',costPerInstallment)