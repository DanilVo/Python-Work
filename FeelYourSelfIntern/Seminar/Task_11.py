# Сформировать список из  N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.



n = 5
j = 1
for i in range(0,n):
    j *=-3
    print(j)