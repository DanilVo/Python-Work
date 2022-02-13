# Найти сумму чисел от 1 до А
def x():
    a = int(input('enter num: '))
    count = 0
    for i in range(a+1):
        count = count + i
    print(count)
x()