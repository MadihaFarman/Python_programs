def main():
    with open('coffee.txt','r') as readfile:
        descr = readfile.readline()
        while descr!='':
            qty = readfile.readline()
            descr = descr.rstrip('\n')
            qty = qty.rstrip('\n')
            print(f'Description # {descr}\nQuantity # {qty}')
            descr = readfile.readline()
main()
