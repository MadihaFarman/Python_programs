import circle
import rectangle
CIRCLE_AREA_CHOICE = 1
CIRCLE_CIRCUMFERENCE_CHOICE = 2
RECTANGLE_AREA_CHOICE = 3
RECTANGLE_PERIMETER_CHOICE = 4
QUIT_CHOICE = 5
def main():
 choice = 0
 while choice!=QUIT_CHOICE:
    #display menu
    display_menu()
    choice = int(input('Enter your choice number: '))
    if choice == CIRCLE_AREA_CHOICE:
        radius = float(input('Enter radius of the circle: '))
        print('Area of circle with radius',radius,'is:',circle.area(radius))
    elif choice == CIRCLE_CIRCUMFERENCE_CHOICE:
        radius = float(input('Enter radius of the circle: '))
        print('Circumference of circle with radius',radius,'is:',circle.circumference(radius))
    elif choice == RECTANGLE_AREA_CHOICE:
        length = float(input('Enter length of rectangle: '))
        width = float(input('Enter width of rectangle: '))
        print('Area of rectangle with length of',length,'and width of',width,'is:',rectangle.area(length,width))
    elif choice == RECTANGLE_PERIMETER_CHOICE:
        length = float(input('Enter length of rectangle: '))
        width = float(input('Enter width of rectangle: '))
        print('Perimeter of rectangle with length of',length,'and width of',width,'is:',rectangle.perimeter(length,width))
    elif choice == QUIT_CHOICE:
        print('Exiting the program.......')
    else:
        print('Invalid input!')

def display_menu():
    print('  MENU ')
    print('1)Area of circle.\n2)Circumference of circle.\n3)Area of rectangle.\n4)Parameter of rectangle.\n5)Quit')

main()
# r = float(input('enter r: '))
# my_circle_area = circle.area(r)
# print('area : ', my_circle_area)