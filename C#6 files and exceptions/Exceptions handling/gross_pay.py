try:
    hours = int(input('Enter hours worked : '))
    pay_rate = float(input('Enter pay rate : '))
    gross_pay = hours*pay_rate
    print(f'Gross pay for {hours} hours is Rs.{gross_pay}')
except ValueError:
    print("ERROR: Hours worked and pay rate must be valid numbers.")