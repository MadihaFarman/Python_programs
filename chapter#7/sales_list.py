days = int(input('Enter number of days : '))
sales = [0] * days
index = 0
print('Enter sales amount for each day:')
while index < days:
    print(f'Day # {index+1} : ',end='')
    sales[index] = float(input())
    index +=1
print('Here are the values entered: ')
for value in sales:
    print(value)
#print('The list is: ',sales)
