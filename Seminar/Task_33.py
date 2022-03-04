# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = 3
lst = [random.randint(0, 100) for i in range(k + 1)]
print(lst)

li = []
for i in range(len(lst)):
    li.append(str(lst[i]) + '*x ^ ' + str(k - i) + ' + ')

li.pop()
li.append(str(lst[-1]))
li.append(' = 0')
text = ''.join(li)
print(text)


with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(text)
