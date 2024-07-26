def main():
    with open('cities.txt','r') as infile:
      cities = infile.readlines()
      index = 0
    while index < len(cities):
       cities[index] = cities[index].rstrip('\n')
       index += 1
    print(cities)

      
main()
            