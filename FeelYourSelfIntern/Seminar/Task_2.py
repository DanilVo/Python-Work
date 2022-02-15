# Найти максимальное из пяти чисел

import random
from tkinter import N

list = []
for i in range(0,10):
    n = random.randint(0,100)
    list.append(n)
print(f'{list}\n{max(list)} is the largest number')
    