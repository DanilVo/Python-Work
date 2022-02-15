# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

n = int(input())
if n%30 ==0:
    print('wrong')
elif n % 5 == 0 and n % 10 == 0 or n % 15 == 0:
    # if n % 30 == 1:
        print('it is')
else:
    print('it is not')

# n = int(input())
# if not n%5 and not n % 10:
#     if n % 30 == 0:
#         print('ok')