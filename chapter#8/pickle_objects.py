import pickle
def main():
    again = 'y'
    with open('info.dat','wb') as output_file:
     while again =='y' or again == 'Y':
        save_data(output_file)
        again = input('Want to add more data: (y for yes): ')
def save_data(file):
   person = {}
   person['name'] = input('Name: ')
   person['age'] = int(input('Age: '))
   person['weight'] = float(input('Weight: '))
   pickle.dump(person,file)
main()