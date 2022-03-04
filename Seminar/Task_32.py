# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]
list =  [1, 2, 3, 5, 1, 5, 3, 10]
list1 = []
for i in range(len(list)):
    list1.append(set(list))
print(list1)

list =  [1, 2, 3, 5, 1, 5, 3, 10]
list1 = []
for i in range(len(list)):
    if not list[i] in list1:
        list1.append(list[i])
print(list1)

