def main():
    names_list = []
    control = 'y'
    while control == 'y':
        name = input('Enter name : ')
        names_list.append(name)
        print('Do you want to add other names ?')
        control = input('(\'y\'=yes, \'n\'=no): ')
    print('The names you entered are :')
    for name in names_list:
        print(name)
    print('The names list is : ',names_list)
main()