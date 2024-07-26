total = 0.0
try:
    with open('sales.txt','r') as outfile:
        for line in outfile:
            amount= float(line)
            total += amount
            print(format(total, '.2f'))
except IOError:
    print('ERROR: An error accured while trying to read data from the file.')
except ValueError:
    print('Non-numeric data found in the file')
except:
    print('An error occured.')