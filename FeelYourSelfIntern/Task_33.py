# Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

import random
list = [None]*12
newList = []
for i in range(12):
    list = random.randint(0, 12)
    newList.append(list)
print(newList)
pos = 0
neg = 0
for j in len(newList):
    if newList[j] % 2 ==0:
        pos = pos + newList[j]
print(pos)
