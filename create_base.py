import sqlite3
import os


dirname=os.path.dirname(__file__)
os.chdir(dirname)

connection = sqlite3.connect("base.db")

cursor = connection.cursor() 

cursor.execute("CREATE TABLE IF NOT EXISTS tab_1(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,  age INTEGER, city TEXT)")
pipls=(("Ваня", 19, "Благовещенск"),("Петя", 13, "Белогорск"),("Аня", 18, "Зея"),("Саша", 21, "Свободный"),("Настя", 19, "Благовещенск"))
cursor.executemany("INSERT INTO tab_1 (name, age, city) VALUES (?, ?, ?)", pipls)

connection.commit()


cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, user_group TEXT)")
users=(("Администратор","123", "Администратор"),("Пользователь - 1",  "111", "Пользователь"), ("Пользователь - 2",  "111", "Пользователь"))
cursor.executemany("INSERT INTO tab_2 (username, password, user_group) VALUES (?, ?, ?)", users)

connection.commit()

connection.close()






