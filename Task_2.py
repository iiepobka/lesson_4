# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для
# формирования списка использовать генератор.

task_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []
for i in range(1, len(task_list)):
    if task_list[i] > task_list[i - 1]:
        result.append(task_list[i])

print(result)

# другой вариант
result_1 = [task_list[number] for number in range(1, len(task_list)) if task_list[number] > task_list[number - 1]]

print(result_1)
