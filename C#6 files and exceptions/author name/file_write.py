def main():
    #opening a file in w mode. if file dosen't exist, it will create it ,otherwise will open existing file and  erase all its pre-existing contents.
    out_file = open('authorNames.txt','w')
    #writing names of 3 authors to the file
    out_file.write('Nemrah Ahmed\nUmera Ahmed\nSadia Rajpoot\n')
    #closing the file
    out_file.close()
main()
