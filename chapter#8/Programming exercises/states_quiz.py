import random
def main():
    states_dic = {'KPK':'Peshawar','Punjab':'Lahore','Balochistan':'Quetta','Sindh':'Karachi','Gilgit Baltistan':'Gilgit'}
    correct = 0
    incorrect = 0
    states = list(states_dic.keys())
    random.shuffle(states)
    for state in states:
     answer = input(f'The capital of {state} is : ')
     if answer.strip().lower() == states_dic[state].strip().lower():
        print('Correct')
        correct+=1
     else:
        print('Incorrect')
        incorrect+=1
    print(f'Number of correct questions: {correct}')
    print(f'Number of incorrect questions: {incorrect}')
main()

        