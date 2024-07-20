n=4
for r in range(n):
    for x in range(0,n-r,1):
        print(' ',end='')
    for y in range(0,2*r-1,1):
        print('*',end='')
    print() 
for r in range(n,0,-1):
   for y in range(0,2*r-1,1):
     print('*',end='')
   for x in range(0,n-r,1):
    print(' ',end='')
   print()               