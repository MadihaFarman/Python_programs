def main():
    intro()
    cups_needed = int(input("enter number of cups: "))
    
    cups_to_ounces(cups_needed)
def intro():
    print('This program converts cups to ounces!')
def cups_to_ounces(cups):
    ounces = cups*8
    print(cups,' cups converted to ounce equals',ounces,'ounces.')
main()
     
    


