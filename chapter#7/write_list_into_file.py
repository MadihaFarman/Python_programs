def main():
    cities = ['Kohat','Peshawar','Islamabad','Faisalabad','Quetta','Lahore']
    with open('cities.txt','w') as outfile:
        for city in cities:
            outfile.write(city + '\n')
main()