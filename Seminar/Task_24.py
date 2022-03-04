# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

list = [1.1, 1.2, 3.1, 5, 10.01]
max = list[0]%1
min = 0
for i in list:
    if i%1 > max:
        max = i%1
        max = round(max,2)
    if i > min:
        min = i%1
        min = round(min, 2)
print(max - min)



# max = 1.2
# min = 10.01

# max_full = max//1
# min_full = min//1

# max1 = max - max_full
# min1 = min - min_full

# result = max1 - min1
# print(round(result,2))