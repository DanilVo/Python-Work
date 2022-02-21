# Вычислить число pi c заданной точностью d
# 	Пример: при d = 0.001,  = 3.141. 
import math

n = str(input('enter float number'))
a = int(len(n))
print(round(math.pi,a-2 ))