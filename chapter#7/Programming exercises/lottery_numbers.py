import random
def main():
 lottery_number = [0] * 7
 for index in range(0,7):
  lottery_number[index] = random.randint(0,9)
 print('Numbers list is : ',lottery_number)
 for num in lottery_number:
  print(num)
main()