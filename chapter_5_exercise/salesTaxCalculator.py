STATE_SALES_TAX = 0.05
COUNTRY_SALES_TAX = 0.025
def main():
    monthly_sales = float(input('Enter monthly sales: '))
    amount_of_state_tax = state_tax(monthly_sales)
    amount_of_country_tax = country_tax(monthly_sales)
    total_sales_tax = total_tax(amount_of_state_tax,amount_of_country_tax)
    print('Monthly Sales :',monthly_sales)
    print('The amount of county sales tax :',amount_of_country_tax)
    print('The amount of state sales tax :',amount_of_state_tax)
    print('Total sales tax :',total_sales_tax)
def state_tax(sales):
    return sales * STATE_SALES_TAX
def country_tax(sales):
    return sales * COUNTRY_SALES_TAX
def total_tax(tax1,tax2):
    return tax1 + tax2
main()