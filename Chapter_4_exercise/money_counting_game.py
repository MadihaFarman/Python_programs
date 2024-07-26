print('Enter coins to make one dollar : ')
pennies = int(input('Enter number of pennies : '))
nickles = int(input('Enter number of nickles : '))
dimes = int(input('Enter number of dimes : '))
quarters = int(input('Enter number of quarters : '))
total_value = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
ONE_DOLLAR = 1.0
if total_value == ONE_DOLLAR:
    print('Congratulations! You have entered exactly one dollar. You win the game!')
elif total_value<ONE_DOLLAR:
    print(f"The total value of the coins is ${total_value:.2f}, which is less than one dollar.")
elif total_value>ONE_DOLLAR:
    print(f"The total value of the coins is ${total_value:.2f}, which is more than one dollar.")    