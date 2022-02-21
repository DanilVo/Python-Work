# Задать список из n чисел последовательности (1+1/n)n и вывести на экран их сумму

n = int(input())
sum = 0
for i in range(0,n):
    sum += (1+1/n)**n
    print(sum)