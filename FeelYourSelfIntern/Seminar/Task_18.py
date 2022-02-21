# Реализовать алгоритм перемешивания списка. 

import random


list = [0,1,2,3,4,5,6,7,8,9]
list1 = []
for i in range(len(list)):
    list1.append(list[random.randint(0,len(list)-1)])
    list1 = random.sample(range(len(list)), len(list))
print(list1)
