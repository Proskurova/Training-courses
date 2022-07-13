# создать список случайных чисел (-20, 50) на 30 элементов
# написать алгоритмы сортировки: по возрастанию, по убыванию
# по количеству делителей числа  ( 15 - 1, 3, 5; 30 - 1, 2, 3, 5, 6, 15) -> [15, 30, ...]
import random
random_number = [random.randint(-20, 50+1) for i in range(30)]
print("Рандомный список:", random_number)
random_number.sort()
print("Рандомный список по возрастанию:", random_number)
random_number.sort(reverse=True)
print("Рандомный список по убыванию:", random_number)
a = []
deliteli = 0
for i in random_number:
    for j in range(1, i+1):
        if i % j == 0:
            deliteli += 1
    a.append(deliteli)
    deliteli = 0
random_number_dictionary = dict(zip(random_number, a))
sorted_tuple = sorted(random_number_dictionary.items(), key=lambda x: x[1])
print("Список по количеству делителей числа с делителем:", sorted_tuple)

