# Выяснить, кратно ли число заданному, если нет, вывести остаток.

num = int(input('enter first num: '))
num1 = int(input('enter second num: '))
if num/num1 == (num//num1)*1.0:
    print('could division')
else:
    print((num/num1))