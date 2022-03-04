# Найти НОК двух чисел

a = int(input('enter a: '))
b = int(input('enter b: '))
num1 = []
num2 = []
for i in range(1,b):
    num1.append(a*i)
    num2.append(b*i)
for j in range(len(num1)):
    if num1[j] in num2:
        print(num1[j])