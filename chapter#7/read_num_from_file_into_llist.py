def main():
    with open('numbersList.txt','r') as infile:
        numbers = (infile.readlines())
        index = 0
        while index < len(numbers):
            numbers[index] = int(numbers[index].rstrip('\n'))
            index +=1
        print(numbers)
main()
