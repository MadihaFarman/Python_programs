seconds = int(input('Enter the number of seconds : '))
if seconds>=60 and seconds<3600:
    minutes = seconds//60
    remaining_seconds = seconds%60
    print(f'Minutes = {minutes}   Remaining seconds = {remaining_seconds}')
elif seconds>=3600 and seconds<86400:
    hours = seconds//3600
    remaining_min = (seconds%3600)//60
    remaining_sec = (seconds%3600)%60
    print(f'Hours = {hours}\nMinutes = {remaining_min}\nSeconds = {remaining_sec} ')
elif seconds>=86400:
    days = seconds//86400
    seconds_left = seconds%86400
    remaining_hours = seconds_left//3600
    seconds_left = seconds_left%3600
    remaining_min = seconds_left//60
    remaining_sec = seconds_left%60
print(f'Days = {days}\nHours = {remaining_hours}\nMinutes = {remaining_min}\nSeconds = {remaining_sec}')
