# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 10))

print(numbers)

# Подсчет количества совпадающих элементов
count = {}
for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

print("Количество совпадающих элементов:", sum(count.values()))

# Удаление повторяющихся элементов
unique_numbers = list(set(numbers))
print(unique_numbers)