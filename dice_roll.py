

import random


print('Roll The Dice!')
print(f'dice 1: {random.randint(1,5)}')
print(f'dice 2: {random.randint(1,5)}')
j = int(input('\nDo you wnt to roll again?\nYes: 1\nNo: 2\n'))
while j != 2:
    if j == 1:
        print(f'Dice 1: {random.randint(1,7)}')
        print(f'Dice 2: {random.randint(1,7)}')
        j = int(input('\nDo you wnt to roll again?\nYes: 1\nNo: 2\n'))
if j == 2:
    print('Have a good day!')