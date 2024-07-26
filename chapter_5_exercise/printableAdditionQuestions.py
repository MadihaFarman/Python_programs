import random
def main():
   for i in range(1,6):
     print(' Question #',i)
     print(generate_numbers())

def generate_numbers():
  number1 = random.randint(1,10)
  number2 = random.randint(1,10)
  return f"{number1} + {number2} = {'--------'}"   
main()
