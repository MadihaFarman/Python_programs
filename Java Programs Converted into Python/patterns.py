'''the code below prints this pattern: 
* 
* *
* * *
* * * *
* * * * *'''
# n = int(input('Enter number of rows in pyramid: '))
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print('* ',end='')
#     print()
'''the code snippet below prints this pattern:
1  
1  2
1  2  3
1  2  3  4
1  2  3  4  5'''
# n = int(input('Enter number of rows in pyramid: '))
# for rows in range(1,n+1):         #used range=1,n+1 so that counting starts from 1 and end on the number that we have given as n. If it was only 'n', then it would print 1 less than n bcz the lasst limmit is not included
#     for cols in range(1,rows+1):     #similaR AS above[(1,rows+1)]
#         print(cols,' ',end='')
#     print()
''' the program below prints this pattern:
1 
2  3  
4  5  6
7  8  9  10'''
# n = 4
# number = 1
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         print(number,' ',end='')
#         number +=1
#     print()
''' the code below prints this pattern:
1 
0 1 
1 0 1
0 1 0 1
1 0 1 0 1'''
# n=5
# for rows in range(1,n+1):
#     for cols in range(1,rows+1):
#         sum = rows+cols
#         if (sum%2==0):
#             print('1 ',end='')
#         else:
#             print('0 ',end='')
#     print()
'''this code snippet prints the following pattern:
1  2  3  4  5
1  2  3  4
1  2  3
1  2
1'''
# n=5
# for rows in range(1,n+1):
#     for cols in range(1,(n-rows+1)+1):
#         print(cols,' ',end='')
#     print()
'''code snippet below the pattern prints the respective pattern:
*      *
**    **
***  ***
********
***  ***
**    **
*      * '''
# n=4
# for rows in range(n):
# #printing stars of first portion(upper half)
#     for cols in range(rows):
#         print('*',end='')
# #printing spaces for upper half
#     spaces = 2*(n-rows)
#     for j in range(spaces):
#         print(' ',end='')
# #printing stars for second portion of upper half
#     for cols in range(rows):
#         print('*',end='')
#     print()        
# for rows in range(n,0,-1):
#     for cols in range(rows):
#         print('*',end='')
# #printing spaces for upper half
#     spaces = 2*(n-rows)
#     for j in range(spaces):
#         print(' ',end='')
# #printing stars for second portion of upper half
#     for cols in range(rows):
#         print('*',end='')
#     print() 
'''following pattern is printed by code below:
     * * * * * 
    * * * * * 
   * * * * *
  * * * * *
 * * * * * 
    '''       
# n=5
# for rows in range(n):
#     #printing spaces
#     spaces = n-rows
#     for space in range(spaces):
#         print(' ',end='')
#     #printing stars
#     for stars in range(n):
#         print('* ',end='')
#     print()
'''the code below prints this pattern:
    1
   2 2
  3 3 3
 4 4 4 4 
'''
# n=5
# for rows in range(n):
#     #printing spaces
#     spaces = n-rows
#     for space in range(spaces):
#         print(' ',end='')
#     for num in range(rows):
#         print(rows,'',end='')
#     print()
