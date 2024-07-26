for row in range(8):
    for col in range(6):
        if (row==0 or row==7 or col==0 or col==5):
         print('*',end='')
        else:
           print(' ',end='') 
    print()