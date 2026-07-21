print('_____________')
print('KPH\tMPH')
print('_____________')
for kph in range(60, 140, 10):
    mph = kph * 0.6214
    print(f'{kph}\t{mph:.1f}')