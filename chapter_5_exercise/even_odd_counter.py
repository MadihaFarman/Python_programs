import random
def main():
   even_odd_check()
def even_odd_check():
    even_counter = 0
    odd_counter = 0
    for i in range(1,101):
        num = random.randint(1,100)
        print(num)
        if num%2==0:
            print('Even')
            even_counter +=1
        else:
            print('Odd')
            odd_counter +=1
    print('Number of evens :',even_counter)
    print('Number of odds :',odd_counter)
    

main()      
    