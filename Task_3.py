# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить
# задание в одну строку.

multiple_numbers = [number for number in range(20, 240) if number % 20 == 0 or number % 21 == 0]
print(multiple_numbers)