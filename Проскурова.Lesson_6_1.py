# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.
List1 = [15, 48, 'hello', 6, 19, 'world']
lines = ''
vowels = 0
consonant = 0
for i in List1:
    if type(i) == int:
        if i % 2 == 0:
            a1 = i % 10
            b1 = i // 10
            print("Сумма цифр четного числа:{0}".format(a1+b1))
        else:
            List1[List1.index(i)] = 1
    else:
        lines += i
print("Замена нечетных чисел на '1': {0}".format(List1))
for j in lines:
    if j in "aeiouy":
        vowels +=1
    else:
        consonant +=1
print("Количество гласных звуков:{0}.\nКоличество согласных звуков:{1}".format(vowels, consonant))