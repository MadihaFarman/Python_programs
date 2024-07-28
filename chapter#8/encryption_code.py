codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '8',
        'D': '*', 'd': '7', 'E': '(', 'e': '6', 'F': ')', 'f': '5',
        'G': '_', 'g': '^', 'H': '-', 'h': '4', 'I': '+', 'i': '3',
        'J': '=', 'j': '2', 'K': '[', 'k': '1', 'L': ']', 'l': '0',
        'M': '{', 'm': '}', 'N': '|', 'n': '\\', 'O': ':', 'o': ';',
        'P': '"', 'p': "'", 'Q': '<', 'q': '>', 'R': ',', 'r': '.',
        'S': '?', 's': '/', 'T': '!', 't': '~', 'U': '`', 'u': 'Z',
        'V': 'X', 'v': 'C', 'W': 'V', 'w': 'B', 'X': 'N', 'x': 'M',
        'Y': 'Q', 'y': 'W', 'Z': 'E', 'z': 'R', ' ': '_','.' : '!'
    }
st = input('Enter a string to be encrypted: ')
for ch in st:
          value_of_ch = codes.get(ch,' ')           
          print(f'{value_of_ch}',end='') 
print()                     
# decryption code:                                                  
reverse_codes = {}                                                                                                         
for k,v in codes.items():   
       reverse_codes[v] = k
#print(reverse_codes)
encrypted_string = input('\nEnter an encrypted string to be decrypted: ')
for ch in encrypted_string:
        value_of_ch = reverse_codes.get(ch,' ')          
        print(f'{value_of_ch}',end='')



          
