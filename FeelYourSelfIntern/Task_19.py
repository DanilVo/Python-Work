# Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
if x > 0 and y > 0:
    print('first quarter')
if x > 0 and y < 0:
    print('second quarter')
if x < 0 and y < 0:
    print('third quarter')
if x < 0 and y > 0:
    print('fourth quarter')