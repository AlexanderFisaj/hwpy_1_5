# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

from random import randint

# метод заполнения списка случайными значениями
def fillingList (lst):
    for _ in range(10):
        lst.append(randint(1, 11))

# метод определения следующее большего в списке
def NextIndexLargerNumber(lst, next):    
    for i in range(next, len(lst) - 1):        
        if lst[next] < lst[i]:
            return i
    return None

# создаем список 
numbers = [1, 5, 2, 3, 4, 6, 1, 7]
# заполняем список
# fillingList(numbers)
# выводим заполненный список в терминал
print(f'Исходный массив: {numbers}')

# создаем список для заполнения полученными элементами
increasing_numbers = []
# генерируем случайный элемент начального списка
my_random_index = randint(0, len(numbers) - 1)
# добавляем случайный элемент в результирующий список
increasing_numbers.append(numbers[my_random_index])

# print(f'Первое заполнение результирующего массива {increasing_numbers}')
# print('-----------------------------------------------------------------')
# тестовый вывод
# print(f'Рандомный вход: {my_random_index}\nСтартовое число для сравнения: {numbers[my_random_index]}')
# print('-----------------------------------------------------------------')
# заполнение результирующего списка элементами по возрастанию без изменения порядка расположения в первичном списке

while my_random_index < len(numbers):
    index = NextIndexLargerNumber(numbers, my_random_index)
    # print(f'Срез: {numbers[(my_random_index):]}')
    if index != None:
        increasing_numbers.append(numbers[index])        
        # print(f'Этот индекс должен измениться: {my_random_index}')
    else:
        break
    my_random_index = index
    
    
    


print(increasing_numbers)