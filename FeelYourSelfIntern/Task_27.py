# Определить количество цифр в числе

num = int(input('enter your number: '))
count = 1 
while 1<num>9:
    num = num//10
    count = count+1
print(count)