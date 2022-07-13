# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def summ(numb1, numb2):
    return numb1 + numb2
def minn(numb1, numb2):
    return numb1 - numb2
def mul(numb1, numb2):
    return numb1 * numb2
def div(numb1, numb2):
    if numb2 == 0:
        return "На ноль делить нельзя!"
    else:
        return numb1 / numb2


while True:
    try:
        numb1, numb2 = float(input("Введите 1 число: ")), float(input("Введите 2 число: "))
    except ValueError:
        print("Нужно вводить только цифры!")
        continue
    x = input("Введите любую операцию +, -, /, *: ")
    if x == '+':
        print('Сумма чисел: ', summ(numb1, numb2))
    elif x == '-':
        print('Разность чисел: ', minn(numb1, numb2))
    elif x == '*':
        print('Произведение чисел: ', mul(numb1, numb2))
    elif x == '/':
        print('Частное чисел: ', div(numb1, numb2))
    else:
        print('Вводите правильно операцию!')
    exit_ = input("Если захотите выйти из программы нажмите ноль: ")
    if exit_ == "0":
        break
    else:
        print("Продолжаем!")
