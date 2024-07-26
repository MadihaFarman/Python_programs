def main():
    num_emp = int(input('How many employees record do you want to save: '))
    with open('employee_records.txt','w') as outfile:
        for count in range(1,num_emp+1):
            print(f'Enter details for employee # {count} :')
            name = input('Name # ')
            ID = input('ID # ')
            dept = input('Department # ')
            outfile.write(name + '\n')
            outfile.write(ID + '\n')
            outfile.write(dept +'\n')
            print()
        print('Employees record written to employee_records.txt.')
main()