def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers = []
    for number in numbers:
        if number>=0 and number<=100:
            valid_numbers.append(number)
    print('List of valid numbers is: ',valid_numbers)
    sum = total(valid_numbers)
    avrg = average(sum,valid_numbers)
    print('Total of valid numbers is : ',sum)
    print('Average of valid numbers is : ',format(avrg,'.2f'))
        
def total(nums_list):
    total = 0
    for num in nums_list:
        total +=num
    return total
def average(sum,nums_list):
    return sum/len(nums_list)
main()