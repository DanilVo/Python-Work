# Определить, присутствует ли в заданном списке строк, некоторое число

list = ['123sdasd', '345fgfd', '5345fsdfgf']
n = input('set symbol to find: ')
for i in list:
    if n in i:
        print('it is')
    else:
        print('not there')

# import math
# def f(x):
#     return x*x

# list = [1,2,3,5,8,15,23,38]

# list1 = [(i, f(i)) for i in list if i % 2 == 0]
# print(list1)