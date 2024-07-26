def main():
    another = 'y'
    with open('coffee.txt','a') as coffee_file:
     while another == 'y' or another == 'Y':
        print('Enter following details about coffe: ')
        descr = input('Enter description : ')
        qty = float(input('Enter quantity in pounds : '))
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')
        print('Do you want to add another record?')
        another = input('(y=yes, any other=no) : ')
    print('data appended to coffee.txt')
main()