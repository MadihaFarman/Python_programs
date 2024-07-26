speed_mph = float(input('Enter speed of the car in mph : '))
hours_traveled = int(input('Enter number of hours traveled : '))
print(f'{'Hour Number':15}{'Distance Traveled':18}')  #specifying field width
for i in range(1,hours_traveled+1):
    distance = speed_mph * i
    print(f'{i}\t\t\t{distance}')