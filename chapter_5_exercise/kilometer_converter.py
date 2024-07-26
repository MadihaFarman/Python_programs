def main():
    km = float(input('Enter kilometers to be converted into miles: '))
    miles = km_to_miles(km)
    print(km,'km =',miles,'miles.')
def km_to_miles(km):
    return km * 0.6214
main()

     