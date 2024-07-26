ASSESSMENT_PERCENTAGE = 0.6
PROPERTY_TAX = 0.72
def main():
    property_piece_price = float(input('Enter property price : '))
    assessment = assessment_value(property_piece_price)
    print('Assessment value =',assessment)
    tax =property_tax(assessment)
    print('Property Tax =',format(tax,'.2f'))
def assessment_value(property_price):
    return property_price * ASSESSMENT_PERCENTAGE
def property_tax(assessment):
    return assessment/100 * PROPERTY_TAX
main()