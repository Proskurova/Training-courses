# Task 1. Создать две таблицы в одной базе данных.
# Одна таблица будет содержать текстовые данные в единственной колонке (не считая id),
# вторая таблица только числовые данные в единственной колонке (не считая id).
# В любом месте кода создайте список (например sp = [1,2,3,4,10,100,1000, 'one' , 'potato', 'carrot'],
# в котором будут числа и слова.
# Ну а теперь - что с этим делать:
# 1.1 В текстовую таблицу закинуть все слова, а в числовую все числа.
# 1.2 В числовой таблице удалить все строки, где число больше 10.
# 1.3 В текстовой таблице все строки со словами длиннее 4 символов обновить на фразу 'Overone‘

import sqlite3
list_ = [25, 'purpose', 5, 'one', 7, 16, 'motivation', 'action', 1, 2, 3, 'achievements', 12, 100, 'put']
int_, str_ = [], []
for i in list_:
    if type(i) is str:
        str_.append(i)
    elif type(i) is int:
        int_.append(i)
conn = sqlite3.connect('Proskurova.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)''')
conn.commit()
for i in str_:
    cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?)''', (i,))
    conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
c = cursor.fetchall()
print(c)
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
conn.commit()
for i in int_:
    cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?)''', (i,))
    conn.commit()
cursor.execute('''SELECT * FROM tab_2''')
k = cursor.fetchall()
print(k)
for i in c:
    i = list(i)
    if len(i[1]) > 4:
        cursor.execute('''UPDATE tab_1 SET col_1 = 'Overone' WHERE id =?''', (i[0],))
        conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
c = cursor.fetchall()
print(c)
for i in k:
    i = list(i)
    if i[1] > 10:
        cursor.execute('''DELETE FROM tab_2 WHERE id = ?''', (i[0],))
        conn.commit()
cursor.execute('''SELECT * FROM tab_2''')
k = cursor.fetchall()
print(k)