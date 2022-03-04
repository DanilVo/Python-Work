# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

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