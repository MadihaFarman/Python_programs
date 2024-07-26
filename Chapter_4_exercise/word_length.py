words = [] #creating an empty list to store words entered by the user
while True:
    word = input('Enter a word or press enter to finish: ')
    if word=='': #This conditional statement checks if the word variable is an empty string. 
        break   #In Python, an empty string evaluates to False in boolean contexts, so this check is used to determine if the user pressed Enter without typing anything.
    words.append(word)
if words:   #if words: means if words ==True---> means if words list is not empty, then proceed
 total_length = sum(len(word) for word in words) #find the length of each word in the words list and sum them up
 average_length=total_length/len(words)  #len(words): finds the number of words in the words list
 rounded_average = round(average_length) #rounds the result
 print(f'The average length of words entered is : {rounded_average}')
else:
   print('No words were entered.')