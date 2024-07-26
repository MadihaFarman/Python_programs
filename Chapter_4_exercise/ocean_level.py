rising_rate_per_year = 1.6
print(f'{'Year':6} {'Level raised':15}')
for i in range(1,26):
    ocean_rising_each_year = format(i * rising_rate_per_year,'.2f')
    print(f'{i:<6}{ocean_rising_each_year:>7} mm')