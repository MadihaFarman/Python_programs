vegeterian=input('Is anyone in your party a vegetarian?(yes/no) ')
vegan = input('Is anyone in your party a vegan?(yes/no) ')
gluten_free = input('Is anyone in your party gluten-free?(yes/no) ')
if vegeterian=='yes'and vegan=='yes' and gluten_free=='yes':
    print('Here are your resturant choices:\nCorner Cafe\nThe Chef\'s Kitchen')
elif vegeterian=='yes'and vegan=='no' and gluten_free=='yes':
    print('Here are your resturant choices:\nMain Street Pizza Company\nCorner Cafe\nThe Chef\'s Kitchen')
elif vegeterian=='no'and vegan=='no' and gluten_free=='no':
    print('Here is your resturant choice :\nJoe\'s Gourmet Burgers') 
else:
     print('Here is your resturant choice :\nMama\'s Fine Italian')



