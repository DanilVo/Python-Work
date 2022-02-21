# Строка содержит набор чисел. Показать большее и меньшее число. Символ-разделитель - пробел

from re import S


str = "123 234 345 456 543 432 41 64 325 56"
str1 = [i for i in str.split(' ')]
for j in range(len(str1)):
    str1[j] = int(str1[j])
max_num = max(str1)
min_num = min(str1)
print(max_num , min_num)
