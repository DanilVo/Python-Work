# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] 

n = 4
permanent = 1
list = []
for i in range(1,n+1):
    permanent *= i
    list.append(permanent)
print(list) 

