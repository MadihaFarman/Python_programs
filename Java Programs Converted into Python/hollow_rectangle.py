length = int(input('Enter length: '))
width = int(input('Enter width: '))
for rows in range(length):
    for cols in range(width):
        if(rows==0 or rows==length-1 or cols==0 or cols==width-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()