# 4.Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
a = ''.join((" An apple a day keeps the doctor away".lower()).split())
d = {i: a.count(i) for i in a}
print(d)