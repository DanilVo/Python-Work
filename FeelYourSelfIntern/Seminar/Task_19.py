# Реализовать алгоритм задания случайных чисел. Без использования встроенного 
# генератора псевдослучайных чисел	

# n = int(input('enter number: '))
# list = []
# for i in range(0,5):
#     list.append(i*n)
#     print(list)
import time
def random_number(minimum,maximum):
    now = str(time.process_time())
    rnd = float(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)
random_number(1,10)