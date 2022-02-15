# Вывести на экран числа от -N до N

n = int(input('-'))
for i in range(-n,n):
    n += 1
    print(i+1)