count = 0
sentence = input('Enter a string : ')
for ch in sentence:
    if ch == 'T' or ch == 't':
        count+=1
print('Number of ts in the given string is : ',count)