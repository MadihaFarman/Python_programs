def main():
    found=False
    search = input('Enter description that you want to search: ')
    with open('coffee.txt','r') as coffee_file:
        descr = coffee_file.readline()
        while descr !='':
            qty = float(coffee_file.readline())
            descr = descr.rstrip('\n')
            if descr == search:
                print('Description : ',descr)
                print('Quantity : ',qty)
                print()
                found = True
            descr = coffee_file.readline()
    if not found:                                         
        print('That item was not found in the file.')
main()