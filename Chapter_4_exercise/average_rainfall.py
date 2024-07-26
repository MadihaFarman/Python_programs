years = int(input('Enter number of years : '))
total_inches_rainfall = 0
for i in range(1,years+1):
    print(f'Year # {i}')
    for j in range(1,13):
        inches_of_rain_perMonth = int(input(f'Enter number of inches of rainfall for month number {j} : '))
        total_inches_rainfall +=inches_of_rain_perMonth
num_of_months = 12*years
average_inches_perMonth = format(total_inches_rainfall/num_of_months,'.2f')
print(f'Number of years = {years}')
print(f'Number of Months = {num_of_months}')
print(f'Total inches of Rainfall = {total_inches_rainfall} inches')
print(f'Average rainfall Per Month = {average_inches_perMonth} inches')
