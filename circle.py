import math
radius = float(input('Enter radius of circle: '))
area = math.pi * radius**2
circumference = 2*math.pi*radius
print('Area of circle of radius',radius,'is',format(area , '.2f'))
print('Circumference of circle of radius',radius,'is',format(circumference , '.2f'))