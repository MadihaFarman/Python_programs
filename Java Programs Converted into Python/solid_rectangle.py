length = int(input('Enter length: '))
width = int(input('Enter width: '))
for rows in range(length):
    for cols in range(width):
        print('*',end='')
    print()            