def main():
    numbers = get_values()
    print('The numbers in the list are : ')
    print(numbers)
def get_values():
    my_list = []
    again = 'y'
    while again=='y':
        num = int(input('Enter number to add to the list: '))
        my_list.append(num)
        print('Do you want to add another number?')
        again = input('y=yes , n=no : ')
    return my_list
main()