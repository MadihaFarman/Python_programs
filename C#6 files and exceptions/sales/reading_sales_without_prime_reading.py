def main():
    infile = open('sales.txt','r')
    for line in infile: 
        sales = float(line)
        print(format(sales,'.2f'))
    infile.close()
main()
'''
for line in infile:
The loop will iterate once for each line in the file.
The first time the loop iterates,
variable will reference the first line
in the file (as a string), the second 
time the loop iterates, variable will
reference the second line, and so forth
'''