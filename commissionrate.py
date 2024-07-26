def main():
    sales = get_sales()
    advanced_pay = get_advanced_pay()
    commission_rate = determine_commission_rate(sales)
    pay = sales * commission_rate - advanced_pay
    print('Pay is $',format(pay,'.2f'),sep='')
    if pay<0:
        print('Talk to the CEO!')
def get_sales():
    sales = float(input('Enter monthly sales: '))
    return sales
def get_advanced_pay():
   advance = float(input(('Enter amount of advance, if no advance taken, enter 0\nAdvanced amount: ')))
   return advance
def determine_commission_rate(sales):
    if sales < 10000.00:
       rate = 0.10
    elif sales >= 10000 and sales <= 14999.99:
       rate = 0.12
    elif sales >= 15000 and sales <= 17999.99:
       rate = 0.14
    elif sales >= 18000 and sales <= 21999.99:
        rate = 0.16
    else:
       rate = 0.18
    return rate
main()




