x = int(input("enter x value: "))
match x:
    case 0:
        print('X is zero')
    case 1:
        print("X is one")
    case _ if x!=4:
        print(x,"is not four!")    
    case _: 
        print(x)      