import login
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    id_number = input('Enter your student id number: ')
    print('Your campus system login username is : ',end='')
    print(login.get_login_name(first_name,last_name,id_number))
main()