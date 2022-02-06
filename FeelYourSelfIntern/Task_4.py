# Найти максимальное из трех чисел

num1 = int(input('enter first num: '))
num2 = int(input('enter second num: '))
num3 = int(input('enter third num: '))
if num1 > num2:
    max = num1
else:
    max = num2
if max > num3:
    print(max)
else:
    print(num3)
