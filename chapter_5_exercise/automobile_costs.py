def main():
    print('Enter the following details: ')
    loan = float(input('Enter loan: '))
    insurance = float(input('Enter insurance amount: '))
    oil = float(input('Enter gas oil expenditure: '))
    tires = float(input('Enter tires expenditure: '))
    cost = float(input('Enter maintainance costs: '))
    costsPerMonth = monthly_costs(loan,insurance,oil,tires,cost)
    print('Monthly costs =',costsPerMonth)
    print('Yearly cost =',yearly_costs(costsPerMonth))
def monthly_costs(loan,insurance,oil,tires,maintainance):
    return loan+insurance+oil+tires+maintainance
def yearly_costs(costPerMonth):
    return costPerMonth * 12
main()