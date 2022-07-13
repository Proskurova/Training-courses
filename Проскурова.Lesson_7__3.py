# Задача 3. На входе пользователь дважды вводит несколько чисел через пробел.
# На выходе - вывести совпадающие числа в порядке возрастания
number1, number2 = input("Введите несколько чисел через пробел:"), input("Введите сново несколько чисел через пробел:")
number1, number2 = set(number1.split(" ")), set(number2.split(" "))
matches = list(number1.intersection(number2))
matches1 = []
for i in matches:
    if i.isdigit():
        i = int(i)
        matches1.append(i)
matches1.sort()
print(matches1)