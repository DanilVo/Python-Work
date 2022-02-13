# Показать четные числа от 1 до N

from ast import Num


n = int(input('enter your num: '))
for x in range(1, n):
    if x % 2 == 0:
            print(x)  