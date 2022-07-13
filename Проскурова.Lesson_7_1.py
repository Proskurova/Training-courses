# Задание №1. Найти самое длинное слово в строке.
string1 = "I am sure learning foreign languages is very important nowadays"
print(string1)
string2 = list(string1.split(" "))
number_s = []
count = 0
for i in string2:
    count += len(i)
    number_s.append(count)
    count = 0
dictionary = dict(zip(string2, number_s))
for k, z in dictionary.items():
    if z == max(dictionary.values()):
        print("Самое длинное слово:{0}, в нем {1} букв".format(k, z))