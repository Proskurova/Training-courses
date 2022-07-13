# 4. Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
import math
a = int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))
c = int(input("Введите 3 число:"))
d = int(input("Введите 4 число:"))
e = int(input("Введите 5 число:"))
f = int(input("Введите 6 число:"))
j = int(input("Введите 7 число:"))
k = int(input("Введите 8 число:"))
l = int(input("Введите 9 число:"))
n = int(input("Введите 10 число:"))
list = [a, b, c, d, e, f, j, k, l, n]
for i in list:
    if i == 0:
        list.remove(i)
print(math.prod(list))
