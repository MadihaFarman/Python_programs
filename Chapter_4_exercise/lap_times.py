total_time=0
lap_times = []  #It initializes an empty list to store the lap times.
num_of_times_of_rounds= int(input('Enter number of times of runs that you have made : '))
for i in range(1,num_of_times_of_rounds+1):
    lap_time=float(input(f'Enter lap time for lap number {i}: '))
    total_time +=lap_time
    lap_times.append(lap_time) #Each lap time is appended to the lap_times list.
fastest_lap = min(lap_times)
lowest_lap = max(lap_times)
print(f'Time of fastest lap = {fastest_lap}')
print(f'Time of slowest lap = {lowest_lap}')
average = total_time/num_of_times_of_rounds # OR ---->
#average_lap = sum(lap_times) / num_of_times_of_rounds  
print('Average lap time = ',average)
#print(lap_times) #it prints the list(all the lap times)