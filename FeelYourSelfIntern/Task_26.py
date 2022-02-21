# Возведите число А в натуральную степень B используя цикл

num1 = int(input('enter your num: '))
num2 = int(input('enter second num: '))
bow = 1

for i in range (1,num2+1):
    bow = bow * num1
print(bow)
