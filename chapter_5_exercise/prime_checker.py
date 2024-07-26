def main():
   number = int(input('Enter a number to check if it is prime or not : '))
   print('Prime Number : ',is_prime(number))
   #printing all the prime numbers from 1 to 100
#    for i in range(1,101):
#        if is_prime(i)== True:
#         print(i)
       
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
    #for i in range(2,n+1):
        if n % i == 0:
            return False
    return True
main()