# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
count = 0
j = str(input('num: '))
k = str(input('num: '))
for i in range(0,len(j)):
    if j[i] in k:
        count += 1
print(count)

