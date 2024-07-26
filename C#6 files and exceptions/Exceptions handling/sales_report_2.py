total = 0.0
try:
    with open('sales.txt','r') as outfile:
        for line in outfile:
            amount= float(line)
            total += amount
            print(format(total, '.2f'))
except Exception as x:
    print(x)