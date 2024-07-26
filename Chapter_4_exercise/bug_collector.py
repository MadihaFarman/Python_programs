total = 0
for i in range(1,6):
    daily_bugs=int(input(f'Enter bugs collected on day {i} of the five days: '))
    print('Bugs collected on day',i,'=',daily_bugs)
    total +=daily_bugs
print()    
print('Bugs collected in five days =',total)
