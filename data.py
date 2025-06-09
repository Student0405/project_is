from tkinter import END, DISABLED, NORMAL
import datetime

def save_data(tree, log_file, E_name, E_age, E_city, L_id, B_del, B_edit, B_Enter, connection, cursor):
    
    name = E_name.get()
    age  = E_age.get()
    city = E_city.get()
    
    cursor.execute("UPDATE tab_1 SET name=?, age=?, city=? WHERE id=?", (name, int(age), city, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)

    B_del.config(state=NORMAL)
    B_edit.config(state=NORMAL)
    B_Enter.config(text="Ввод", command=lambda:  add_data(tree, E_name, E_age, E_city, log_file, connection, cursor))
    L_id.config(text="IID:")

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} изменена\n")

def del_data(tree, log_file, connection, cursor):
    data = tree.item(tree.selection())
    data_ID=data["values"][0]
    cursor.execute(f"DELETE FROM tab_1 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {data_ID} удалена\n")
    

def edit_data(tree, log_file, E_name, E_age, E_city, L_id, B_del, B_edit, B_Enter, connection, cursor):
    global id
    iid = tree.selection()
    
    
    id = tree.item(iid)["values"][0]
    name = tree.item(iid)["values"][1]
    age = tree.item(iid)["values"][2]
    city = tree.item(iid)["values"][3]

    L_id.config(text=id)

    E_name.insert(0, name)
    E_age.insert(0, age)
    E_city.insert(0, city)

    B_del.config(state=DISABLED)
    B_edit.config(state=DISABLED)
    B_Enter.config(text="Сохранить", command=lambda: save_data(tree, log_file, E_name, E_age, E_city, L_id, B_del, B_edit, B_Enter, connection, cursor))

def add_data(tree, E_name, E_age, E_city, log_file, connection, cursor):
    

    name = E_name.get()
    age = E_age.get()
    city = E_city.get()
        
    
    
    cursor.execute("INSERT INTO tab_1 (name, age, city) VALUES (?, ?, ?)", (name, int(age), city))
    connection.commit()
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_1")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)    
    
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} добавлена\n")
        
    E_name.delete(0, END)
    E_age.delete(0, END)
    E_city.delete(0, END)