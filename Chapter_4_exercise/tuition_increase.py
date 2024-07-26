TUITION_FEE_PER_SEMESTER = 8000
INCREASE_RATE = 0.03
fee = TUITION_FEE_PER_SEMESTER
print(f'{'Year':6} {'Increased Fee':15}')
#print(f'{1:<6}{8000.00:<10}')
for i in range(2,6):
    fee = (fee*INCREASE_RATE) + fee
    print(f'{i:<6}{fee:>10.2f}')


