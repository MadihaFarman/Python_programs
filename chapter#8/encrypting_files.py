codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '&', 'c': '8',
    'D': '*', 'd': '7', 'E': '(', 'e': '6', 'F': ')', 'f': '5',
    'G': 'v', 'g': '^', 'H': '-', 'h': '4', 'I': '+', 'i': '3',
    'J': '=', 'j': '2', 'K': '[', 'k': '1', 'L': ']', 'l': '0',
    'M': '{', 'm': '}', 'N': '|', 'n': '\\', 'O': ':', 'o': ';',
    'P': 'z', 'p': "'", 'Q': '<', 'q': '>', 'R': ',', 'r': '.',
    'S': '?', 's': '/', 'T': '!', 't': '~', 'U': '`', 'u': 'Z',
    'V': 'X', 'v': 'C', 'W': 'V', 'w': 'B', 'X': 'N', 'x': 'M',
    'Y': 'Q', 'y': 'W', 'Z': 'E', 'z': 'R', ' ': '_', '.': 'Y',
    '\n': 'x', ',': ';'
}

with open('text.txt','r') as outfile_1:
    content = outfile_1.read()
#print(content)
with open('encrypted_text.txt','w') as outfile_2:
    for ch in content:
      value_of_ch = codes.get(ch,' ')
      outfile_2.writelines(value_of_ch)         
       
       