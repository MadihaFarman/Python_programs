import random
HEAD = 1
TAIL = 2
TOSSES = 10
for toss in range(TOSSES):
    number = random.randint(1,2)
    if number==1:
        print('Head')
    else:
        print('Tail')