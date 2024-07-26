def main():
    with open('employee_records.txt','r') as infile:
     #for line in infile:
     name = infile.readline()
     while name != '':
        id = infile.readline()
        dept = infile.readline()
        # Strip the newlines from the fields
        name = name.rstrip('\n')
        id = id.rstrip('\n')
        dept = dept.rstrip('\n')
        # Display the record
        print(f'Name # {name}')
        print(f'Emplyee ID # {id}')
        print(f'Department # {dept}')
        print()
        name = infile.readline()
main()
        
