import math
people = int(input('How many people are attending the cookout ? '))
hot_dogs_per_head = int(input('Enter number of hot dogs per head : '))
HOT_DOG_PKG = 10
HOT_DOG_BUNS_PKG = 8
required_hot_dogs = people * hot_dogs_per_head
required_buns = people * hot_dogs_per_head
min_hotDogs = math.ceil(required_hot_dogs/HOT_DOG_PKG)
min_buns = math.ceil(required_buns/HOT_DOG_BUNS_PKG)
left_over_hotDogs = (HOT_DOG_PKG*min_hotDogs) - required_hot_dogs
left_over_buns = (HOT_DOG_BUNS_PKG*min_buns) - required_buns
print(f'Minimum number of packages of hot dogs required = {min_hotDogs}')
print(f'Minimum number of packages of hot dog buns required = {min_buns}')
print(f'Number of hot dogs that will be left over = {left_over_hotDogs}')
print(f'Number of hot dog buns that will be left over = {left_over_buns}')