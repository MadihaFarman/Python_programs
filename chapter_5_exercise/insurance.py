PERCENTAGE = 0.80
def main():
    replacement_cost = float(input('Enter replacement cost for your property: '))
    print('Minimum amount of insurance :',insurance_amount(replacement_cost))
def insurance_amount(replacementCost):
    return replacementCost * PERCENTAGE
main()
