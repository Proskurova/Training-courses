# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова,
# то выводить все гласные, иначе согласные;
# Eсли передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
class Detection:
    def __init__(self, str_numb):
        self.str_numb = str_numb

    def func2(self):
        return len(self.str_numb)

    def func1(self):
        if not self.str_numb.isdigit():
            gl, sl = 0, 0
            for i in self.str_numb:
                if i in 'AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя':
                    gl += 1
                elif i in ''' .,:;"?'!-()/''':
                    continue
                else: sl += 1
            if gl*sl <= self.func2():
                print('Количество гласных: ', gl)
            else:
                print('Количество согласных: ', sl)
        elif type(self.str_numb) == str and self.str_numb.isdigit():
            chet = 0
            for i in self.str_numb:
                i = int(i)
                if i % 2 == 0:
                    chet += i
                else:
                    continue
            print('Произведение четных чисел на длину числа: ', chet * self.func2())


detection = Detection(str_numb=input('Введите строку или число: '))


detection.func1()



