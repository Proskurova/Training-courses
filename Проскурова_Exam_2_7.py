# 7.Напишите программу, демонстрирующую работу try\except\finally

# Я создала: Программа, которая находит все простые числа от a до b включительно,
# а затем выводит сумму простых чисел от a до b, деленную на число введенное пользователем.
while True:
    a, b = input("Введите первое число:"), input("Введите второе число:")
    try:
        a = int(a)
        b = int(b)
        if a > b:
            print("Первое число должно быть меньше!")
            continue
        c = [i for i in range(a, b+1) if not [j for j in range(2, i) if not i % j]]
        print(c)
        break
    except ValueError:
        print("Нужно вводить только цифры!")
    finally:
        print("Продолжем!")
try:
    z = float(input("Введите число:"))
    res = sum(c)/z
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
except ValueError:
    print("Нужно вводить только цифры!")
else:
    print("Результат деления: ", res)

