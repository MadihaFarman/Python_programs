numberOfStudents = int(input('Enter number of students: '))
numberOfTests = int(input('Enter number of tests per student: '))
for student in range(numberOfStudents):
    total = 0.0
    print('Student number',student+1)
    print('-------------------')
    for test_num in range(numberOfTests):
        print('Test Number',test_num+1,end='')
        score = float(input(': '))
        while score<0 or score>100:
         print('Error: Enter correct score!')
         print('Test Number',test_num+1,end='')
         score = float(input(': '))
         total += score
         average = total / numberOfTests
    print('The average for student number',student+1,'is: ',format(average,'.2f'))
    print()