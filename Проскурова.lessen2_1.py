# Задача №1: Определить, является ли год високосным
a = int(input('Введите год:'))
if a%400==0:
    print('Високосный')
elif a%100==0:
    print('Невисокосный')
elif a%4==0:
    print('Високосный')
else:
    print('Невисокосный')
