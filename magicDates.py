month = int(input('ENter month : '))
print('Type of month is: ',type(month))
day = int(input('Enter day : '))
year = int(input('ENter year : '))
magic_date = month * day
if year ==magic_date:
    print('Date is magic!')
else:
    print('Date is not magic!')