from tkinter import *
from tkinter import ttk
import mysql.connector

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)

#load data to dropdowan box
cursor = mydb.cursor()
cursor.execute("SELECT CID,CName FROM classdetails")
data = cursor.fetchall()

root=Tk()
root.title('Add New Student - LearnMaster 1.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/stregisterSmall.png')
Label(root,
      image=img,
      bg='white').place(x=90,y=80)

#add frame for form
frame = Frame(root,
              width=450,
              height=500,
              bg='white')
frame.place(x=450,y=5)

#add label
label = Label(frame,
              text="Add New Student",
              fg='#57a1f8',
              bg='white',
              font=('Microsoft YaHei UI Light',25,'bold'))
label.place(x=95,y=0)

#entry box for name
def on_enter(e):
    name.delete(0,'end')
    
def on_leave(e):
    name1=name.get()
    if name1=='':
        name.insert(0,'Name')
        
name = Entry(frame,
             width=50,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
name.place(x=30,y=75)
name.insert(0,'Name')
name.bind('<FocusIn>',on_enter)
name.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=410,
      height=2,
      bg='black').place(x=25,y=102)

#entry box for email
def on_enter(e):
    email.delete(0,'end')
    
def on_leave(e):
    name=email.get()
    if name=='':
        email.insert(0,'Email')
        
email = Entry(frame,
             width=50,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
email.place(x=30,y=145)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=410,
      height=2,
      bg='black').place(x=25,y=172)

#add drop box
def on_select(e):
    selectedItem = dropdown.get()
    
selectedItem = StringVar()

dropdown = ttk.Combobox(frame,
                        textvariable=selectedItem,
                        state="readonly",
                        font=('Microsoft YaHei UI Light',11),
                        width=30)
dropdown['values'] = [item[1] for item in data]
dropdown.set("Select Subjects")
dropdown.place(x=30,y=215)
dropdown.bind('<<ComboboxSelected>>',on_select)

#add button
addbtn = Button(frame,
                text="Add",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2')
addbtn.place(x=330,y=207)

#add table



root.mainloop()