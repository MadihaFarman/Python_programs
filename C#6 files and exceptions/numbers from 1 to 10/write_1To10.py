def main():
    with open('writingNumbers.txt','w') as outfile:
        for i in range(1,11):
            num = i
            outfile.write(str(num) + '\n')
main()