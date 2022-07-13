# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу
f = open('Проскурова_Exam.txt', 'w')
f.write('Klemcheck Oleg 2\nKeslyack Olga 9\nMozgo Ivan 7\nStepnoy Leon 1\nSafonova Alla 10\nCherepanova Glasha \
10\nNikiforov Ruslan 2\nProskurova Lyuda 10')
f.close()
with open('Проскурова_Exam.txt',) as f:
    txt = f.readlines()
c = 0
for i in txt:
    if i[-1] == "\n":
        i = i[:-1]
    if int(i.split()[-1]) < 3:
        print(i)
    c += int(i.split()[-1])
    bal = c/len(txt)
print("Средний балл по классу: {0:.2f}".format(bal))