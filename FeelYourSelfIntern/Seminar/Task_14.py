# Подсчитать сумму цифр в вещественном числе.

num = input('enter your num: ')
sum = 0
for i in range(0,len(num)):
    if num[i] != '.':
        sum += int(num[i])
print(sum)