pocket_num= int(input("enter a pocket number (1 to 36): "))
if pocket_num ==0:
    print(f'Pocket number {pocket_num} is green!')
elif pocket_num>=1 and pocket_num<=10:
    if pocket_num%2==0:
        print(f'Pocket number {pocket_num} is black!')
    else:
        print(f'Pocket number {pocket_num} is red!')
elif pocket_num>=11 and pocket_num<=18:
    if pocket_num%2==0:
        print(f'Pocket number {pocket_num} is red!')
    else:
        print(f'Pocket number {pocket_num} is black!')
elif pocket_num>=19 and pocket_num<=28:
    if pocket_num%2==0:
        print(f'Pocket number {pocket_num} is black!')
    else:
        print(f'Pocket number {pocket_num} is red!')
elif pocket_num>=29 and pocket_num<=36:
    if pocket_num%2==0:
        print(f'Pocket number {pocket_num} is red!')
    else:
        print(f'Pocket number {pocket_num} is black!')
else:
    print('ERROR: Invalid Input.\nEnter a number in between 0 and 36.')

