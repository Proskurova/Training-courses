# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
a = ['language', '1', '23', 'increasing', 'stupid', 'music', '48', 'servant', 'telephone',
     '50', '39', 'term', '15']
str_ = []
number = []
for i in a:
    if i.isdigit():
        number.append(int(i))
    elif i.isalpha():
        str_.append(i)
str_.sort(key=len)
number.sort()
print(str_, number)
f = open('Проскурова.txt', 'w')
for i in str_:
    f.write(i+ '\n')
for j in number:
    f.write(str(j)+ '\n')
f.close()
