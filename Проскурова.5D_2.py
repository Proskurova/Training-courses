# создать еще один список чисел ( рандомное количество элементов)
# найти вывести: пересечения двух списков, уникальные элементы одного и второго
import random
random_number = [random.randint(-20, 50+1) for i in range(30)]
print("Рандомный список:", random_number)
random_number2 = [random.randint(-20, 50+1) for j in range(20)]
print("Второй рандомный список:", random_number2)
random_number.extend(random_number2)
unique_number = []
for i in random_number:
    if random_number.count(i) <= 1:
        unique_number.append(i)
print(unique_number)


