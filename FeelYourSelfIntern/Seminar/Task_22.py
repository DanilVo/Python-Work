# Найти сумму чисел списка стоящих на нечетной позиции

# list = [1,2,3,4,5,6,7]
# sum = 0
# for i in range(0,len(list)):
#     if list[i]%2==1:
#         sum+=list[i]
# print(sum)

list = [1,2,3,4,5,6,7]
sum = 0
for i in range(0,len(list),2):
    sum+=list[i]
print(sum)

# list = []
# for i in range(1,6):
#     n = int(input())
#     list.append(n)
# print(list)