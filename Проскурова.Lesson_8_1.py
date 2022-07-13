# Задача №1
# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.
A = [[0] * 5 for i in range(5)]
import random
for i in range(5):
    for j in range(5):
        A[i][j] = random.randint(1, 30)
        print(A[i][j], end=" ")
    print()
C = []
c = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        c += A[i][j]
    C.append(c)
    c = 0
print(C)
print("Mаксимальная сумма элементов: ", max(C), ", Номер строки в матрице: ", C.index(max(C)))
