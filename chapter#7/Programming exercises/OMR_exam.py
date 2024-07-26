correct_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
student_answers_list = []
incorrect_answers_question_number_list = []
correct_count = 0
incorrect_count = 0
print('Correct answers list is :\n',correct_answers)
with open(r'C:\Users\Farman\Desktop\python programs\chapter#7\Programming exercises\student.txt','r') as outfile:
     #for index in range(len(correct_answers)):
     for index in range(len(correct_answers)):
          student_answer = outfile.readline().rstrip('\n')
          student_answers_list.append(student_answer)
          if correct_answers[index] == student_answers_list[index]:
               correct_count +=1
          else:
               incorrect_count +=1
               incorrect_answers_question_number_list.append(index+1)
                 
     print('Student answers list is :\n ',student_answers_list)
     if correct_count>=15:
               print('The student passed the exam.')
     else:
               print('The student failed the exam.')
     print('Number of correctly answered questions : ',correct_count)
     print('Number of incorrectly answered questions : ',incorrect_count)
     print('Incorrectly answered question numbers list is : ',incorrect_answers_question_number_list)
                    
          


