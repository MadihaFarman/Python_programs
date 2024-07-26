print(f'{'Miles':10}{'Kilometers':15}')
for i in range(10,81,10):
    miles_to_km = format(i * 1.60934,'.2f')
    print(f'{i:<10}{miles_to_km:<15}')

