year = int(input('Enter year : '))
#if year%100==0 and year%400==0 or year%4==0 and year%100!=0:
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f'{year} is a leap year.\nIn {year} Feburary has 29 days.')
else:
    print(f'{year} is not a leap year.\n{year} Feburary has 28 days.')
