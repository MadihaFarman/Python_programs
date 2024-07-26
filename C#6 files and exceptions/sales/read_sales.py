def main():
    infile = open('sales.txt','r')
    # Read the first line from the file, but
    # don't convert to a number yet. We stil
    # need to test for an empty string.
    line = (infile.readline())
    while line!= '':
        sales = float(line)
        print(format(sales,'.2f'))
        line = infile.readline()
    infile.close()
main()
    