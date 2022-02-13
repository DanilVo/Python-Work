# Дано число из отрезка [10, 99]. Показать наибольшую цифру числа

import random
num = random.randint(10,99)
print('the chosen one is: ', num)
num1 = num%10
num2 = num//10
if num1>num2:
    print(num1,'is the biggest')
else:
    print(num2,'is the biggest')