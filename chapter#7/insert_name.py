def main():
    names = ['Madiha','Fariha','Muhammad','Hamza']
    print('The names list before editing is : \n',names)
    name = input('Enter name that you want to insert: ')
    name_index = int(input('Enter the index at which you want to insert the name: '))
    names.insert(name_index,name)
    print('List has been updated.\nList after updation is: \n',names)
main()