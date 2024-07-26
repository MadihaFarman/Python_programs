n = int(input('Enter value of number upto which you want to calculate the sum: '))
sum = 0
for number in range(n+1):   
  sum = sum + number
 #print(number)
print('Sum of first',n,'natural numbers is:',sum)
