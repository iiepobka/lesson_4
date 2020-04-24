# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного;
# б) итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import count
from itertools import islice
from itertools import cycle

# Вариант a
start_number = int(input('Введите число - начало генерации целых чисел: '))
last_number = int(input('Введите последнее число последовательности: '))

for number in count(start_number):
    if number > (last_number):
        break
    else:
        print(number)

# Или такое решение варианта а
count_numbers = int(input('Введите кол-во членов последовательности: '))

for number in islice(count(start_number), count_numbers):
    print(number)


# Или такое решение варианта а
def add(x, y):
    for i in range(x, y):
        yield i


for i in add(2, 5):
    print(i)

# Вариант б
my_list = [number for number in range(2, 7, 2)]
max_count = int(input('Введите число - колличество итераций цикла: '))
start_count = 0

for item in cycle(my_list):
    if start_count > max_count:
        break
    print(item)
    start_count = start_count + 1
