# Составить список простых множителей натурального числа N

num = int(input('enter your num: '))
for i in range(num):
    num //=2
    print(num)