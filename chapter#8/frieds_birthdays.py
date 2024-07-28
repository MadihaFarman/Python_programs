ADD = 1
LOOKUp = 2
CHANGE = 3
DELETE = 4
QUIT = 5
def main():
 birthdays = {}
 choice = 0
 while choice !=QUIT:
    #display menu
    display_menu()
    #get user choice
    choice = int(input('Enter your choice: '))
    if choice == ADD:
      name = input('Enter name : ')
      dob = input('Enter birthday: ')
      add(name,dob,birthdays)
      print(birthdays)
    elif choice == LOOKUp:
      name = input('Enter name : ')
      lookup(name,birthdays)
    elif choice == CHANGE:
      name = input('Enter name : ')
      dob = input('Enter birthday: ')
      change(name,dob,birthdays)
      print(birthdays)
    elif choice == DELETE:
      name = input('Enter name : ')
      delete(name,birthdays) 
      print(birthdays)     
    
def display_menu():
  print()
  print('Friends and Their Birthdays')
  print('---------------------------')
  print('1. Add a new birthday')
  print('2. Look up a birthday')
  print('3. Change a birthday')
  print('4. Delete a birthday')
  print('5. Quit the program')
  print()
def add(name,dob,birthdays):
     if name not in birthdays:
      birthdays[name] = dob
     else:
       print('Already exists')
def lookup(name,birthdays):
  print(birthdays.get(name,'Not found'))
def change(name,dob,birthdays):
   birthdays[name] = dob
def delete(name,birthdays):
  if name in birthdays:
    del birthdays[name]
  else:
    print('Name not found')

main()
  
  
