# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.


from operator import index


list1 =  ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list = []
n = 'йцу'
for i in range(len(list1)):
    if n == list1[i]:
        list.append(i)
print(list[1])








# list = ['123sdasd', '345fgfd', '5345fsdfgf']
# n = input('set symbol to find: ')
# for i in list:
#     if n in i:
#         print('it is')
#     else:
#         print('not there')
