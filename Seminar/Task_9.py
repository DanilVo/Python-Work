# Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

import random

num = random.randint(1,4)
if num == 1:
    print('x>0 and y>0')
if num == 2:
    print('x>0 and y<0')
if num == 3:
    print('x<0 and y<0')
if num == 4:
    print('x<0 and y>0')