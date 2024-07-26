ONE_FEET = 12
def main():
    ft = float(input('Enter feets : '))
    inches = feet_to_inches(ft)
    print(ft,'feet =',inches,'inches.')
def feet_to_inches(feet):
    return feet * ONE_FEET
main()