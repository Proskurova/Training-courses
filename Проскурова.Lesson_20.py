# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Пользователь ничего не вводит, все 4 вызова функции с соответствующим типом данных должны быть прописаны в коде.
def data_type(a):
    if type(a) == int:
        a = str(a)
        nechet = 0
        for i in a:
            i = int(i)
            if i % 2 != 0:
                nechet += 1
        print('Является числом!В нем нечетных чисел: ', nechet)
    elif type(a) == str:
        letter_ = 0
        for i in a:
            if i.isalpha():
                letter_ += 1
        print('Является строкой!В ней букв: ', letter_)
    elif type(a) == tuple:
        words_len = []
        for i in a:
            if type(i) == str and i.isalpha():
                words_len.append(i)
                words_len.append(len(i))
        print('Является картежем!В ней слова  с длинной: ', *words_len)
    elif type(a) == list:
        digit, let = 0, 0
        for i in a:
            if type(i) == str:
                for j in i:
                    if j.isalpha():
                        let += 1
                    elif j.isdigit():
                        digit += 1
            elif type(i) == int:
                digit += 1
        print('Является списком!В нём букв: ', let, 'и чисел: ', digit)


number = 567897738987222
str_ = "I have already learned 300 words."
tuple_ = (98, 3, 'abc', 'assignment', 'simple', '123', 34)
list_ = [87, 'speech', 'communication', 9, 43, '3', 'sign5']

data_type(number)
data_type(str_)
data_type(tuple_)
data_type(list_)


