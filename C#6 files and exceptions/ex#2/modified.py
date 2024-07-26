def main():
    fileName = input('Enter the name of the file : ')
    with open(fileName,'r') as file:
        lines = file.readlines()
        if len(lines)<5:
            print('The file contains less than 5 lines, therefore displaying whole content: ')
            for line in lines:
                print(line)
                #print(line.rstrip('\n'))
        else:
             print('Displaying 5 lines :')
             for line in lines[:5]:
                 print(line)
             # print(line.rstrip('\n'))
main()
