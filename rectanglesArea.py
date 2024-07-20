length1= int(input('Enter length of rectangle 1: '))
width1 = int(input('Enter width of rectangle 1: '))
length2 = int(input('Enter length of rectangle 2: '))
width2 = int(input('Enter width of rectangle 2: '))
area1 = length1*width1
area2 = length2*width2
if area1>area2:
    print('Area of rectangle 1 i.e',area1, 'is greater than area of rectangle 2 i.e',area2,'!')
elif area2>area1:
    print('Area of rectangle 2 i.e',area2, 'is greater than area of rectangle 1 i.e',area1,'!')
elif area1 == area2:
    print('The areas of both rectangles are same!')
