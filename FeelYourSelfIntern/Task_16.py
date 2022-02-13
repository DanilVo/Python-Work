# Дано число обозначающее день недели. Выяснить является номер дня недели выходным
from calendar import day_name


day_num = int(input('enter your day num: '))
if day_num == 6 or day_num == 7:
    print('weekend')
else:
    print('regular day')