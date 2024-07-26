def main():
    string = input('Enter a string that you want to repeat: ')
    integer = int(input('Enter the times that you want to repeat the string: '))
    result = repeat(string,integer)
    print(result)
def repeat(string,integer):
    # for i in range(integer):
    #     w = print(string,end='')
    # return w     #problem: It returns NONE along with the string repeated.check out why?
    return string*integer
main()
