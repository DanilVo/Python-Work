# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

import math

def mathematical():
    a = float(input('enter a: '))
    b = float(input('enter b: '))
    c = float(input('enter c: '))

    discr = b**2 - 4*a*c
    print(round(discr,2))

    if discr == 0:
        print('x = ', -b/(2*a))
    elif discr > 0:
        x1 = (-b + discr ** 0.5) / (2*a)
        x2 = (-b - discr ** 0.5) / (2*a)
        print(x1, x2)
    else:
        print('no koren')

# mathematical()

def math():
    a = float(input('enter a: '))
    b = float(input('enter b: '))
    c = float(input('enter c: '))

    discr = b**2 - 4*a*c
    print(round(discr,2))

    if discr == 0:
        print('x = ', -b/(2*a))
    elif discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2*a)
        x2 = (-b - math.sqrt(discr)) / (2*a)
        print(x1, x2)
    else:
        print('no koren')
math()