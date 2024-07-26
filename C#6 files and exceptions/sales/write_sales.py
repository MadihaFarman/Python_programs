def main():
    days = int(input('For how many days do you have sales? '))
    infile = open('sales.txt','w')
    for i in range(1,days+1):
        sales_per_day = float(input('Enter sales for day #' +str(i) +': '))
        infile.write(str(sales_per_day)+ '\n')
    infile.close()
    print('Data written to sales.txt.')
main()