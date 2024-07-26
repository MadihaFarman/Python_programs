number = int(input('Enter a number: '))
if number>0:
    if number%2==0:
     print('Positive\nEven')
    else:
       print('Positive\nOdd')
elif number<0:
    if number%2==0:
       print('Negative\nEven')
    else:
       print('Negative\nOdd')
elif number==0:
    print('Zero')
