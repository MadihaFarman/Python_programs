per_day_desired_sleep = 8
total_desired_sleep_PerWeek = 56
total_user_weekly_sleep = 0
for i in range(1,8):
    user_sleeps_perDay = int(input(f'How many hours did you slept on day number {i} of the week : '))
    total_user_weekly_sleep +=user_sleeps_perDay
sleep_debt = total_desired_sleep_PerWeek - total_user_weekly_sleep
if sleep_debt!=0:
    print(f'You have sleep debt of {sleep_debt} hours.\nTake enough sleep to stay healthy.')
else:
    print('Great! you have no sleep debt.\nYou are lucky to have enough sleep.')

