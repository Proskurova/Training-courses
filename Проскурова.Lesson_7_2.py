# Задание №2.Преобразовать текст в список слов с удалением знаков препинания
string1 = "Many communities offer low-priced baseball football, soccer,\
 basketball, gymnastics, swimming and ballet programs for \
children under high school age (14 years or younger)."
print(string1)
string2 = ""
for i in string1:
    if i in '''.,:;"?!-()''':
        continue
    else:
        string2 += i
string2_list = string2.split(" ")
print(string2_list)