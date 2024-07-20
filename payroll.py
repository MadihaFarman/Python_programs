BASE_HOURS = 40
overtime_bonus = 1.5
hours = float(input('Enter hours worked: '))
pay_rate = float(input('Enter pay rate: '))
if hours>BASE_HOURS:
    overtime_pay = (hours-BASE_HOURS)*overtime_bonus*pay_rate
    gross_pay = BASE_HOURS*pay_rate + overtime_pay
else:
   gross_pay = hours*pay_rate  
        
print('Gross pay = $',format(gross_pay, ',.2f'), sep='')