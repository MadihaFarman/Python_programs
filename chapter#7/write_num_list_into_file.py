def main():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    with open('numbersList.txt','w') as outfile:
        for num in numbers:
            outfile.write(str(num) + '\n')
main()
