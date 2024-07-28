def main():
    radius_dic = {'Io':'1821.6','Europa':'1560.8','Ganymede':'2634.1','Callisto':'2410.3'}
    gravity_dic = {'Io': '1.796','Europa': '1.314','Ganymede': '1.428','Callisto' :'1.235'}
    orbital_period_dic = {'Io': '1.769','Europa': '3.551','Ganymede': '7.154','Callisto': '16.689'}
    choice = 'y'
    while choice == 'y':
     moon_name = input('Enter the name of a Galilean moon of Jupiter: ')
     print(f'Orbital period = {orbital_period_dic[moon_name]}')
     print(f'Radius = {radius_dic[moon_name]}')
     print(f'Gravity = {gravity_dic[moon_name]}')
     print(f'Orbital period = {orbital_period_dic[moon_name]}')
     choice = input('Do you want to continue (y = yes) : ')
    
    # for key in radius_dic:
    #     print(f'Moon name : {key}')
    #     print(f'Radius = {radius_dic[key]}')
    #     print(f'Gravity = {gravity_dic[key]}')
    #     print(f'Orbital period = {orbital_period_dic[key]}')
       
main()