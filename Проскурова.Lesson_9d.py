# Добавьте на свой рабочий стол папку,
# в ней создайте 3 текстовых файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
import os
os.mkdir("C:/Users/Пользователь/Desktop/Proskurova")
f = open("C:/Users/Пользователь/Desktop/Proskurova/test_1.txt", "w")
f.close()
f2 = open("C:/Users/Пользователь/Desktop/Proskurova/test_2.txt", "w")
f2.close()
f3 = open("C:/Users/Пользователь/Desktop/Proskurova/test_3.txt", "w")
f3.close()
os.chdir("C:/Users/Пользователь/Desktop/Proskurova")
os.rename("test_1.txt", "rename_1.txt")
os.rename("test_2.txt", "rename_2.txt")
os.rename("test_3.txt", "rename_3.txt")
os.chdir("C:/Users/Пользователь/Desktop/Proskurova")
os.remove("rename_1.txt")
os.remove("rename_2.txt")
os.remove("rename_3.txt")
os.chdir("C:/Users/Пользователь/Desktop")
os.rmdir("Proskurova")

