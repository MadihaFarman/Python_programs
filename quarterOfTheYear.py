month = int(input('Enter month number from 1 to 12: '))
if month>=1 and month<=3:
    print('The month is in the 1st quarter!')
elif month>=4 and month<=6:
    print('The month is in the second quarter!')
elif month>=7 and month<=9:
    print('The month is in the 3rd quarter!')
elif month>=10 and month<=12:
    print('The month is in the 4th quarter!')

else:
    print('Enter valid month i.e 1--->12')