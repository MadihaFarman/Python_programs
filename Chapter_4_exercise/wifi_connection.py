print('Here are the possible solutions listed for your bad WIFI connection :')
print()
answer = 'no'
while answer != 'yes':
 print('Rebot the computer and try to connect.')
 answer = input('Did that fix the prbolem? ').lower()
 if answer =='yes':
    print('Exiting the program.....')
    break
 print('Reboot the router and try to connect')
 answer = input('Did that fix the prbolem? ').lower()
 if answer == 'yes':
     print('Exiting the program.....')
     break
 print('Make sure the cables between the router & modem are plugged in firmly.')
 answer = input('Did that fix the prbolem? ').lower()
 if answer == 'yes':
     print('Exiting the program.....')
     break
 print('Move the router to a new location and try to connect')
 answer = input('Did that fix the prbolem? ').lower()
 if answer == 'yes':
     print('Exiting the program.....')
     break
 else:
   print('Get a new router.')
   break

