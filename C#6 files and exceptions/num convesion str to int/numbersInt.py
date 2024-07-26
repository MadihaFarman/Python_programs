def main():
    outfile = open('numbersInt.txt','w')
 #with open('numbers.txt', 'w') as outfile:
#get inputs
    num1 = int(input('Enter num 1: '))
    num2 = int(input('Enter num 2: '))
    num3 = int(input('Enter num 3: '))
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')
    outfile.close()
    print('Data written to numbersInt.txt.')
main()

