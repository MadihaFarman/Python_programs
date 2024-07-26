def main():
    yearly_record = [0] * 12
    for i in range(12):
        yearly_record[i] = float(input(f'Enter rainfall in inches for month number {i+1} : '))
    print('The list of rainfall each month is: ',yearly_record)
    total = total_rainfall(yearly_record)
    average = average_rainfall(total,yearly_record)
    print('The total rainfall for the year is :',total)
    print('The average monthly rainfall is :',format(average,'.2f'))
    l_r_m = lowest_rainfall_month(yearly_record)
    lrm_index = yearly_record.index(l_r_m)
    h_r_m = highest_rainfall_month(yearly_record)
    hrm_index = yearly_record.index(h_r_m)
    print(f'Month number {lrm_index+1} has the lowest rainfall.')
    print(f'Month number {hrm_index+1} has the highest rainfall.')
def total_rainfall(yearly_record):
    total = 0
    for month in yearly_record:
        total += month
    return total
def average_rainfall(total,yearly_record):
    return total/len(yearly_record)
def lowest_rainfall_month(yearly_record):
    return min(yearly_record)
def highest_rainfall_month(yearly_record):
    return max(yearly_record)
    
main()