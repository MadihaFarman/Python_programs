import csv
#This function validates marks entered by user
def get_marks(number):    
    while True:
     try:
      marks = float(input(f'Subject # {number}: Enter marks : '))
      if 0<=marks<=100:
         return marks
      else:
        print("Error: Marks must be between 0 and 100. Please try again.")
     except ValueError:
             print("Error: Invalid input. Please enter a number between 0 and 100.")
#This function validates credit hours entered by user
def get_creditHours():
   while True:
      try:
         credit_hrs = int(input('Enter Credit hours : '))
         if 1<=credit_hrs<=4:
            return credit_hrs
         else:
            print('Error: Credit hours must be between 1 and 4. Try again.')
      except ValueError:
         print("Error: Invalid input. Please enter a number between 1 and 4.")
#for SGPA
per_semester_credit_hrs = 0
per_semester_GP = 0 #it is the sum of earned grade points of all subjects in a semester.
#for CGPA
all_semesters_ch = []  #it will be containing the credit hours of all semesters
all_semesters_GP = []  #it will be containing the per_semester_gp of all semesters 
semester = 1     #declaring this variable for displaying semester number in later program
again = 'y'      #again variable is for checking while loop execution
while again == 'y' or again == 'Y':
  print(f'SEMESTER : {semester}')
  semester +=1
  if semester == 8:
    break
  semester_Transcript = []   # semester_Transcript will store marks,grade points, credit hours and grade of each subject.
  num_subjects = int(input('How many courses have you taken in this semester : '))
  for i in range(num_subjects):
    subject_marks = get_marks(i+1)   #calling get_marks(number) function and storing marks in subject_marks variable
    credit_hrs = get_creditHours()   #calling get_creditHours() function
    per_semester_credit_hrs+=credit_hrs   #adding credit hours to the per_semester_credit hours so that it contains sum of all ch of a semester.
 #the below code snippet opens gpa_table.csv file in read mode and stores it in conversion_table variable
 #the csv.DictReader(conversion_table) reads each row of the CSV file as a dictionary. Each row's field names
 #(e.g., 'Percentage', 'GradePoints', 'Grade') are the dictionary keys, and the corresponding cell values are the 
 # dictionary values. This makes it easy to access data by column names.
 # (for row in reader) This loop iterates over each row in the CSV file. The DictReader object (reader) 
 # provides each row as a dictionary, with the keys being the column names.
 #(if float(row['Percentage']) == subject_marks:)float(row['Percentage']): This converts the value in the 'Percentage' column of the current row to a float. This conversion is necessary to compare numerical values.
 # == marks: This checks if the converted percentage matches the marks entered by the user. If they match, 
 # the following block of code is executed.(gp, grade = float(row['GradePoints']), row['Grade'])
 # float(row['GradePoints']): This converts the value in the 'GradePoints' column of the current row to a float and assigns it to the variable gp.
 # row['Grade']: This retrieves the value in the 'Grade' column of the current row and assigns it to the variable grade.
    with open('gpa_table.csv', 'r') as conversion_table:
      reader = csv.DictReader(conversion_table)
      for row in reader:    
            if float(row['Percentage']) == subject_marks:
             gp, grade = float(row['GradePoints']), row['Grade']
             print('  |------------------------------|')
             print(f'   Marks : {subject_marks}  |  Grade : {grade}')
             print('  |------------------------------|\n')
      per_subject_GP = credit_hrs * gp    #calculating every subject's grade points
    #appending the below fields to the semester transcript list
    semester_Transcript.append({'Marks': subject_marks,
             'Credit hours': credit_hrs,
             'Earned grade points': per_subject_GP,
             'Grade': grade,
            })
    per_semester_GP += per_subject_GP   #calculating the grade points of whole semester
 #calculating SGPA
  SGPA = per_semester_GP/per_semester_credit_hrs
  print('\n|------------------|')
  print(f'|  SGPA = {SGPA:.2f}     |')
  print('|------------------|')
 #appending whole semester grade points and whole semester credit hours to their respective lists to be further used in CGPA calculation
  all_semesters_ch.append(per_semester_credit_hrs)
  all_semesters_GP.append(per_semester_GP)
 #calculating CGPA
  CGPA = sum(all_semesters_GP)/sum(all_semesters_ch)
  print(f'|  CGPA = {CGPA:.2f}     |')
  print('|------------------|')
  #displaying transcript
  transcript_choice = input('\nDo you want to display transcript?(y for yes and n for no): ')
  if transcript_choice == 'y':
     print(f'\nTranscript for SEMESTER # {semester-1} :')
     print('|-------------------------------------------------------|')
     print("| Marks   | Credit Hours   | Earned Grade Points|Grade  |")
     print('|-------------------------------------------------------|')
     for subject in semester_Transcript:
      print(f"| {subject['Marks']:<7} | {subject['Credit hours']:^13} | {subject['Earned grade points']:^19.2f} | {subject['Grade']:^5} |")
      print('|-------------------------------------------------------|')
     print(f'| SGPA = {SGPA:.2f}             CGPA = {CGPA:.2f}                   |')
     print('|-------------------------------------------------------|')
     #setting the below variables to zero so that they can be used in next semester without containing any pre-data
  per_semester_credit_hrs = 0
  per_semester_GP = 0
  again = input('Do you want to calculate GPA of next semester (y for yes & n for no):  ')