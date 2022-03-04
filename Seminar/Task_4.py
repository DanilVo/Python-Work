# Показать первую цифру дробной части числа

import random

list = []
n = round(float(random.uniform(1, 10)),1)
print(n)
list.append(str(n))
g = list[0]
print(g[2])
