file_name = input('Enter filename: ')
try:
 with open(file_name,'r') as outfile:
    contents = outfile.read()
    print(contents)
except IOError:
   print('ERROR: An error occurred trying to read the file',file_name)

