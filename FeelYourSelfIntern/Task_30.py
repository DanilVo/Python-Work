# Показать кубы чисел, заканчивающихся на четную цифру

num = int(input('enter your num'))
for i in range(2,num+1,2):
    print(i,'**',3,'=',i**3)