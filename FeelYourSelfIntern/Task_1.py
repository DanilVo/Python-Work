#По двум заданным числам проверять является ли первое квадратом второго

num1 = int(input('enter first num: '))
num2 = int(input('enter second num: '))
if num2 / num1 == num1:
    print(True)
else:
    print(False)    
