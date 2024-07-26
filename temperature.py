MAX_TEMP = 102.5
temperature = float(input("Enter temperature of substance in degree celsius: "))
while temperature>MAX_TEMP:
    print('The temperature is too high\nTurn the thermostat down and wait\n5 minutes, then take the temperature and again enter it.')
    temperature = float(input('Enter new tempertaure: '))
print('Temperature is accepatble!')
print('Check it again in 15 minutes!') 
