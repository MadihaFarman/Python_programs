import random    
def main():
   num = int(input('Enter a positive integer : '))
   
   print('The sorted list is : ',roll(num))
def roll(number_of_throws):
     rolls_list = [0] * number_of_throws
     for i in range(number_of_throws):
      rolls_list[i] = random.randint(1,6)
     return rolls_list.sort()
main()