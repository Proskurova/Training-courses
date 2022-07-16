# Описать два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение количества гласных и согласных букв меньше или равно длине слова,
# то выводить все гласные, иначе согласные;
# Eсли передаю число, то вывести произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
class Detection:
    str_n = input('Введите строку или число: ')

    def func1(self):
        if not self.str_n.isdigit():
            gl_l, sl_l = [], []
            gl, sl = 0, 0
            for i in self.str_n:
                if i in 'AEIOUaeiouАЕЁИОУЫЭЮЯаеёиоуыэюя':
                    gl += 1
                    gl_l.append(i)
                elif i in ''' .,:;"?'!-()/''':
                    continue
                else:
                    sl += 1
                    sl_l.append(i)
            if gl*sl <= self.func2():
                print('Гласные: ', gl_l)
            else:
                print('Согласные: ', sl_l)
        elif self.str_n.isdigit():
            chet = 0
            for i in self.str_n:
                i = int(i)
                if i % 2 == 0:
                    chet += i
                else:
                    continue
            print('Произведение четных чисел на длину числа: ', chet * self.func2())

    def func2(self):
        return len(self.str_n)


detection = Detection()


detection.func1()