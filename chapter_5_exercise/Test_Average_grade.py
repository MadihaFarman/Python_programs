def main():
    score_1 = float(input('Enter score of test 1: '))
    score_2 = float(input('Enter score of test 2: '))
    score_3 = float(input('Enter score of test 3: '))
    score_4 = float(input('Enter score of test 4: '))
    score_5 = float(input('Enter score of test 5: '))
    print('Grades of your marks are as follow:')
    print(calc_grades(score_1))
    print(calc_grades(score_2))
    print(calc_grades(score_3))
    print(calc_grades(score_4))
    print(calc_grades(score_5))
    print('\nAverage =',calc_average(score_1,score_2,score_3,score_4,score_5))
    
def calc_average(s1,s2,s3,s4,s5):
    sum = s1+s2+s3+s4+s5
    return sum/5
def calc_grades(score):
    if score>=90 and score<=100:
      return f'Score = {score}\tGrade = A'
    elif score>=80 and score<=89:
      return f'Score = {score}\tGrade = B'
    elif score>=70 and score<=79:
      return f'Score = {score}\tGrade = C'
    elif score>=60 and score<=69:
      return f'Score = {score}\tGrade = D'
    elif score<60:
       return f'Score = {score}\tGrade = F'
    else:
      return 'Invalid input'   
main()