from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as Mbox
root = Tk()

root.title("Welcome to Mobile shop")

root.geometry('600x600')
def insert():
    id = e_id.get()
    brand = e_brand.get()
    model = e_model.get()
    os = e_OS.get()
    processor = e_processor.get()
    ram = e_ram.get()
    battery = e_battery.get()
    price = e_price.get()
    
    if(id == '' or brand == '' or model == '' or os == ''  or processor == '' or ram == '' or battery == '' or price == ''):
        Mbox.showinfo("insert status", "Please fill all fields")
    else:
        conn = mysql.connect(host = 'localhost', user  = 'root', password = 'admin', database = 'mobile_shop')
        cur = conn.cursor()
        cur.execute("insert into phone_db values('"+id+"','"+brand+"','"+model+"','"+os+"','"+processor+"','"+ram+"','"+battery+"','"+price+"')")
        conn.commit()
        Mbox.showinfo("insert status","inserted succesfully")

        e_id.delete(0,'end')
        e_brand.delete(0,'end')
        e_model.delete(0,'end')
        e_OS.delete(0,'end')
        e_processor.delete(0,'end')
        e_ram.delete(0,'end')
        e_battery.delete(0,'end')
        e_price.delete(0,'end')
        conn.close()

def delete():
    if (e_id.get()== ''):
        Mbox.showinfo("Delete status", "Enter ID")
    else:
        conn = mysql.connect(host = 'localhost', user  = 'root', password = 'admin', database = 'mobile_shop')
        cur = conn.cursor()
        cur.execute("delete from phone_db where prodno = '"+e_id.get()+"'")
        conn.commit()
        Mbox.showinfo("Delete status","deleted succesfully")

        e_id.delete(0,'end')
        e_brand.delete(0,'end')
        e_model.delete(0,'end')
        e_OS.delete(0,'end')
        e_processor.delete(0,'end')
        e_ram.delete(0,'end')
        e_battery.delete(0,'end')
        e_price.delete(0,'end')
        conn.close()

def update():
     id = e_id.get()
     brand = e_brand.get()
     model = e_model.get()
     os = e_OS.get()
     processor = e_processor.get()
     ram = e_ram.get()
     battery = e_battery.get()
     price = e_price.get()
    
     if(id == '' or brand == '' or model == '' or os == ''  or processor == '' or ram == '' or battery == '' or price == ''):
        Mbox.showinfo("update status", "Please fill all fields")
     else:
        conn = mysql.connect(host = 'localhost', user  = 'root', password = 'admin', database = 'mobile_shop')
        cur = conn.cursor()
        cur.execute("UPDATE phone_db SET brand = '" + brand + "', model = '" + model + "', processor = '" + processor + "', os = '" + os + "', ram_GB = '" + ram + "', battery_mAh = '" + battery + "', price = '" + price + "' WHERE prodno = '" + id + "'")
        conn.commit()
        Mbox.showinfo("update status","updated succesfully")

        e_id.delete(0,'end')
        e_brand.delete(0,'end')
        e_model.delete(0,'end')
        e_OS.delete(0,'end')
        e_processor.delete(0,'end')
        e_ram.delete(0,'end')
        e_battery.delete(0,'end')
        e_price.delete(0,'end')
        conn.close()



def get():
     
     if (e_id.get()== ''):
        Mbox.showinfo("Fetch status", "Enter valid ID")
     else:
        conn = mysql.connect(host = 'localhost', user  = 'root', password = 'admin', database = 'mobile_shop')
        cur = conn.cursor()
        cur.execute("select * from phone_db where prodno = '"+e_id.get()+"'")
        rows = cur.fetchall()

        for row in rows:
            e_brand.insert(0,row[1])
            e_model.insert(0,row[2])
            e_processor.insert(0,row[3])
            e_OS.insert(0,row[4])
            e_ram.insert(0,row[5])
            e_battery.insert(0,row[6])
            e_price.insert(0,row[7])

        conn.close()




p_id = Label(root, text = "Phone id", font=("bold", 10))
p_id.place(x = 20, y = 20)

p_brand = Label(root, text = "Brand", font=("bold", 10))
p_brand.place(x = 20,y = 60)

p_model = Label(root, text = "Model", font=("bold", 10))
p_model.place(x = 20,y = 100)

p_OS = Label(root, text = "OS", font=("bold", 10))
p_OS.place(x = 20,y = 140)

p_processor = Label(root, text = "Processor", font=("bold", 10))
p_processor.place(x = 20,y = 180)

p_ram = Label(root, text = "RAM", font=("bold", 10))
p_ram.place(x = 20,y = 220)

p_battery = Label(root, text = "Battery", font=("bold", 10))
p_battery.place(x = 20,y = 260)

p_price = Label(root, text = "Price", font=("bold", 10))
p_price.place(x = 20,y = 300)

e_id = Entry()
e_id.place (x = 150,y = 20)

e_brand = Entry()
e_brand.place(x = 150, y = 60)


e_model = Entry()
e_model.place (x = 150,y = 100)

e_OS = Entry()
e_OS.place (x = 150,y = 140)

e_processor = Entry()
e_processor.place (x = 150,y = 180)


e_ram = Entry()
e_ram.place (x = 150,y = 220)


e_battery = Entry()
e_battery.place (x = 150,y = 260)


e_price = Entry()
e_price.place (x = 150,y = 300)

Insert_btn = Button(root, text = "Insert", font = ('italic', 10), command = insert )
Insert_btn.place(x = 20, y = 340)

delete_btn = Button(root, text = "delete", font = ('italic', 10), command = delete )
delete_btn.place(x = 100, y = 340)

update_btn = Button(root, text = "update", font = ('italic', 10), command = update )
update_btn.place(x = 180, y = 340)

search_btn = Button(root, text = "search", font = ('italic', 10), command = get )
search_btn.place(x = 260, y = 340)


root.mainloop()
