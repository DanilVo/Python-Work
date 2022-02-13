# Подсчитать сумму цифр в числе

num = int(input())
sum = 0 
while num >= 1:
    sum = sum + num%10
    num //=10
    print(num)
print(sum)