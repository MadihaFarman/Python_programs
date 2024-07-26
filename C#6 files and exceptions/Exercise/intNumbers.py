def main():
    with open('numbers.txt','w') as number_file:
        for i in range(1,101):
          number_file.write(str(i) + '\n')
    with open('numbers.txt','r') as read_from_file:
       for line in read_from_file:
          line = line.rstrip('\n')
          line = int(line)
          print(line)
          
main()