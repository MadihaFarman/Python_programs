n = int(input('Enter a number to find its factorial: '))
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(f'Factorial of {n} = {factorial}')