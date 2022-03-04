# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#         [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]


list = [1, 5, 2, 3, 4, 6, 1, 7]
new_list = []
for i in range(len(list)):
    cur = list[i]
    if list[i+1] > cur:
        new_list.append(list[i+1])
    print(new_list)











# list = [5, 2, 3, 4, 6, 1, 7] 
# new_list = []
# result = []
# final = [new_list]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# for i in range(len(new_list)):
#     result.append(min(new_list))
#     new_list.pop(0)
# print(result)
