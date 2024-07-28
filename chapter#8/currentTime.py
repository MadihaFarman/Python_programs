import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hours = int(time.strftime('%H'))
print(hours)
minutes = int(time.strftime('%M'))
print(minutes)
seconds = int(time.strftime('%S'))
print(seconds)
if hours < 12:
    print('Good Morning')
elif hours < 15:
    print('Good Afternoon')
elif hours < 18:
    print('Good Evening')
else:
    print('Good Night')
