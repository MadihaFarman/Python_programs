import random
def main():
    ROWS = 3
    COLS = 4
    values = [ [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0] ]
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,100)
    print(values)                          #for printing whole nested/two dimensional list
    # for r in range(ROWS):                #for printing each value on a seperate line
    #     for c in range(COLS):
    #         print(values[r][c])  
    
main()