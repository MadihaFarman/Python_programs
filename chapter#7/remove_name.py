def main():
    names = ['Madiha','Fariha','Muhammad','Hamza']
    print('The names list before editing is : \n',names)
    try:
       name = input('Enter name that you want to remove: ')
       names.remove(name)
       print('List has been updated.\nList after updation is: \n',names)
    except:
        print('Name not found!')
main()