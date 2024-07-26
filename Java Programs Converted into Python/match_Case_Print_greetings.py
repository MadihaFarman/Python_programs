button = int(input('Press Button: '))
match button:
    case 1:
        print('Assalamualikum!')
    case 2:
        print('Hello!')
    case 3:
        print('Namasty!')
    case _:
        print('Press valid button i.e 1 or 2 or 3!')