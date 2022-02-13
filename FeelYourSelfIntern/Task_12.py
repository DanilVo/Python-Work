# Удалить вторую цифру трёхзначного числа

import random
full_num = random.randint(100,1000)
print('before', full_num)
first_num = ((full_num//100)-1)*10
second_num = (full_num % 100)//10
first_num1 = (((full_num//100)*100)-10)+second_num*10
result = full_num-first_num1
result = result +first_num
print('after', result)
