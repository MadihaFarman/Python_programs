number = int(input('Enter a number to check if it is even or odd: '))
if(number%2==0 and number!=0):
    print(number,'is even.')
elif(number==0):
    print('Zero is niether even nor odd.')
else:
    print(number,'is odd.')    