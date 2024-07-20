#Get total number of seconds
total_seconds = float(input('Enter total number of seconds: '))
#calculating total hours
hours = total_seconds // 3600
#calculating remaining minutes
minutes = (total_seconds // 60) % 60
#calculating remaining seconds
seconds = total_seconds % 60
print('The given number of seconds i.e ',total_seconds,' converted into Hours,minutes and seconds: ')
print('Hours : ',hours)
print('Minutes : ',minutes)
print('Seconds : ',seconds)