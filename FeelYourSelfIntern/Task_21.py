# Программа проверяет пятизначное число на палиндромом.

from ctypes.wintypes import INT


num = str(input('enter your num:'))
n = len(num)
if num[0] == num[n-1]:
    print('yes')
else:
    print('it is not polyndrom')
