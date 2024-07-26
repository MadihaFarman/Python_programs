def main():
    infile = open('authorNames.txt','r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
main()