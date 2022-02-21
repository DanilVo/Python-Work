# Задать массив из 8 элементов и вывести их на экран

import random
def fillArray():
    a = int(input('enter A: '))
    b = int(input('enter B: '))
    list = [None]*8
    newList= []
    for i in range(8):
        list = random.randint(a,b)
        newList.append(list)
    print(newList)
fillArray()
