NUM_OF_EMPLOYEES = 3
hourly_rate = float(input('Enter hourly pay rate: '))
hours_list =  [0] * NUM_OF_EMPLOYEES
gross_pay_list = [0] * NUM_OF_EMPLOYEES
for index in range(NUM_OF_EMPLOYEES):
    hours_list[index] = float(input(f'Enter hours worked for Barista {index+1} : '))
for index in range(NUM_OF_EMPLOYEES):
    gross_pay_list[index] = hours_list[index] * hourly_rate
    print(f'Gross pay of barista {index+1} is : ',gross_pay_list[index])
    
print(f'List of Hours worked per barista is : ',hours_list)
print('Gross pay list is : ',gross_pay_list)