# Написать программу преобразования десятичного числа в двоичное


def calc():
    x = int(input('enter your number: '))
    list = [x]
    while x >= 1:
        x //=2
        list.append(x)
    list.pop(len(list)-1)
    return list
list = calc()

def dual(list):
    list1 =[]
    for i in range(len(list)):
        if  list[i]%2 == 0:
            list1.append('0')
        elif list[i]%2 ==1:
            list1.append('1')
    list1.reverse()
    print(list1)
dual(list)


















    # if  x%2 == 1:
    #     list.append('0')
    # elif x%2 ==1:
    #     list.append('1')
# x = [1,2,3,4,5,6,7,8]
# for i in x:
#     print(i)