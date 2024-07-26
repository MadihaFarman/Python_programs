import random
NUMBER_1 = 'rock'
NUMBER_2 = 'paper'
NUMBER_3 = 'scissors'
def main():
 while True:
   user_choice=input('Enter your choice (rock, scissors or paper) : ')
   print('Player choice is: ',user_choice)
   comp_choice = computer_choice()
   print('Computer choice is: ',comp_choice)
   result = decision(comp_choice,user_choice)
   print('Result:\n',result,sep='')
   play_again = input("Do you want to play again? (yes/no): ").lower()   #.lower() converts the input entered into lower case
   if play_again != 'yes':
        break
def computer_choice():
 number = random.randint(1,3)
 if number == 1:
    return NUMBER_1
 elif number ==2:
    return NUMBER_2
 elif number==3:
    return NUMBER_3
def decision(comp_choice,user_choice):
 if comp_choice == 'rock' and user_choice =='scissors' or user_choice =='rock' and comp_choice=='scissors':
    winner = 'rock'
    return f"{winner} wins!"
 elif comp_choice == 'paper' and user_choice=='rock' or user_choice=='paper' and comp_choice=='rock':
    winner = 'paper'
    return f"{winner} wins!"
 elif comp_choice=='scissors' and user_choice=='paper' or user_choice=='scissors' and comp_choice=='paper':
    winner = 'scissors'
    return f"{winner} wins!"
 elif comp_choice==user_choice:
   return f"Game draw!\nPlay again!"
 else:
   return f"Invalid Input!"
 
main()


