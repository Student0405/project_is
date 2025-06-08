from tkinter import ttk
from tkinter import *
from data import del_data, add_data, edit_data
import os
import datetime
import sqlite3

def on_closing():
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Выключение ИС")
    log_file.close()
    connection.close()
    tk.destroy()




dirname=os.path.dirname(__file__)
os.chdir(dirname)


if not os.path.exists("log"):
    os.mkdir("log")

now=datetime.datetime.now()
name = now.strftime("%d.%m.%Y_%H.%M.%S")

log_file=open(rf"log\log_{name}.txt", 'w')



tk = Tk()
tk.title("Таблица")
tk.geometry("750x450+100+100")
tk.protocol("WM_DELETE_WINDOW", on_closing)
    
columns_tuple = ("ID", "name", "age", "city")
tree = ttk.Treeview(tk, columns=columns_tuple, show="headings")


tree.heading("ID", text="ID", anchor="center")
tree.heading("name", text="Имя", anchor="center")
tree.heading("age", text="Возраст", anchor="center")
tree.heading("city", text="Город", anchor="center")

tree.column("ID", width=50, anchor="w") 
tree.column("name", width=200, anchor="w")  
tree.column("age", width=80, anchor="w")
tree.column("city", width=350, anchor="w")


connection = sqlite3.connect("base.db")
cursor = connection.cursor() 

cursor.execute("SELECT * FROM tab_1")

pipls=cursor.fetchall()
connection.commit()

for data in pipls:
    tree.insert("", END, values=data) 


E_name=Entry(tk)
E_age=Entry(tk)
E_city=Entry(tk)

L_name=Label(tk, text="Имя:")
L_age=Label(tk, text="Возраст:")
L_city=Label(tk, text="Город:")

L_id=Label(tk, text="IID:")

B_Enter=Button(tk, text="Ввод", command=lambda: add_data(tree, E_name, E_age, E_city, log_file, connection, cursor))
B_del=Button(tk, text="Удалить", command=lambda: del_data(tree, log_file, connection, cursor))
B_edit=Button(tk, text="Изменить", command=lambda: edit_data(tree,log_file, E_name, E_age, E_city, L_id, B_del, B_edit, B_Enter, connection, cursor))


tree.place(x=10, y=10, height=200)
L_id.place(x=100, y=240)

L_name.place(x=30, y=270)
L_age.place(x=30, y=300)
L_city.place(x=30, y=330)

E_name.place(x=100, y=270, width=160)
E_age.place(x=100, y=300, width=160)
E_city.place(x=100, y=330, width=160)

B_Enter.place(x=30, y=370, width=70)
B_del.place(x=110, y=370, width=70)
B_edit.place(x=190, y=370, width=70)

M=Menu(tk)

M1 = Menu(M, tearoff=0)
M2 = Menu(M, tearoff=0)
M3 = Menu(M, tearoff=0)

M11 = Menu(M1, tearoff=0)

M.add_cascade(label="Файл", menu=M1)
M.add_cascade(label="Правка", menu=M2)
M.add_cascade(label="Справка", menu=M3)

M1.add_cascade(label="Сохранить", menu=M11)
M1.add_separator()
M1.add_command(label="Выход", command=on_closing)

M11.add_command(label="PDF")
M11.add_command(label="TXT")

M2.add_command(label="Создать")
M2.add_command(label="Администрирование")

M3.add_command(label="О программе")
M3.add_command(label="Документация")
tk.config(menu=M)

tk.mainloop()