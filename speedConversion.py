print('KPH\tMPH')
print('-------------')
for KPH in range(60,131,10):
    MPH = KPH*0.6214
    print(KPH,'\t',format(MPH,'.1f'))