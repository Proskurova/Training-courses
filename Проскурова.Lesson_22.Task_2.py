# Task 2. Заполнить таблицу БД названиями песен с указанием их длительности
# (то есть колонка с названием и колонка со временем в минутах)
# Из этой таблицы собрать все записи,
# с длительностью больше 60 минут и записать их в текстовый файл
import sqlite3
song_time = {"Mamma mia": 48, "Move on": 61, "Belly Dancer": 69, "Bones": 59, "Won't Forget You": 65, "Melody": 45,
             "Redrum": 70, "Remedy": 91, "Footprints": 61, "As It Was": 41}
conn = sqlite3.connect('music.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 INTEGER)''')
conn.commit()
for key, val in song_time.items():
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?)''', (key, val))
    conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
music = cursor.fetchall()
print(music)
with open('Lyuda_music', 'w') as f:
    for i in music:
        if i[2] > 60:
            f.write(i[1]+'-'+str(i[2])+' min'+'\n')
with open('Lyuda_music', 'r') as f:
    s = f.readlines()
print(*s)

