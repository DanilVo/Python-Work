# Дано число. Проверить кратно ли оно 7 и 23

num = int(input('enter your num: '))
if num/7 == (num//7)*1.0 and num/23 == (num//23)*1.0:
    print('it is')
else:
    print('cant')