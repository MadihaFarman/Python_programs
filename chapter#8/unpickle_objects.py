import pickle
def main():
    end_of_file = False
    with open('info.dat','rb') as input_file:
        while not end_of_file:
            try:
                person = pickle.load(input_file)
                display_data(person)
                #print(person)
            except EOFError:
                end_of_file = True
def display_data(person):
 print('Name:', person['name'])
 print('Age:', person['age'])
 print('Weight:', person['weight'])
 print()
main()

