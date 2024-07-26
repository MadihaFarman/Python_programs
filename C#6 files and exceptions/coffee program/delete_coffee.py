import os
def main():
    found = False
    search = input('enter the description of the record that you want to delete: ')
    with open('coffee.txt','r') as coffee_file:
        with open('temp.txt','w') as temp_file:
            descr = coffee_file.readline()
            while descr != '':
                qty = float(coffee_file.readline())
                descr = descr.rstrip('\n')
                if descr != search:
                  temp_file.write(descr + '\n')
                  temp_file.write(str(qty) + '\n')
                else:
                  found = True
                descr = coffee_file.readline()
            
    os.remove('coffee.txt')
    os.rename('temp.txt','coffee.txt')
    if found:
       print('The file has been updated')
    else:
       print('That item was not found in the list.')
main()
