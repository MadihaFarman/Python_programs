GRAVITY = 9.8
def main():
    for i in range(1,11):
        x = distance_calculator(i)
        print('When Time =',i,'seconds\nDistance =',format(x,'.2f'),'meters.')
def distance_calculator(time):
    return (1/2)*GRAVITY*time**2
main()