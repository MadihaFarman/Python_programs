def main():
    numbers = [1,2,3,4,5,6,7,8]
    print('The totl is : ',get_total(numbers))
def get_total(values_list):
    total = 0
    for value in values_list:
        total += value
    return total
main()