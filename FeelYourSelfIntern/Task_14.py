# Найти третью цифру числа или сообщить, что её нет

import random
num = random.randint(0,200)
print(num)
if num / 10 >= 10:
    print('third num is:', num % 10)
else:
    print('there is no third num')