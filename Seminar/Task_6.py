# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

list = ['sunday', 'monday', 'thusday','wednesday', 'thursday', 'friday', 'saturday','no such day']
day_number = int(input('enter your day num: '))
print(list[day_number-1])
