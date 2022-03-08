# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt   в одной строке одно число

# list = []
# num =  5
# for i in range(-num,0):
#     list.append(-abs(i))
# for j in range(0,num+1):
#     list.append(abs(j))
# print(list)
# data = open('file.txt', 'w')
# data.writelines(str(-abs(i)))
# data.close()

from tkinter import N


data = open('file.txt', 'w')
num =  5
for i in range(-num,0):
    data.write('\n')
    data.write(str(f'{i} = {-abs(i)}'))
for j in range(0,num+1):
    data.write('\n')
    data.write(str(f'{j} = {abs(j)}'))
data.close()