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

#exit window
def exitwindow():
    root.destroy()
    
#add data to table
def addData():
    subject = dropdown.get()
    sql = "SELECT CID FROM classdetails WHERE CName = %s"
    cursor.execute(sql,(subject,))
    id = cursor.fetchone()
    cid = id[0]
    my_tree.insert('','end',values=(cid,subject))
    

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
                cursor='hand2',
                command=addData)
addbtn.place(x=330,y=207)

#add table
my_tree = ttk.Treeview(frame,height=6)
my_tree['columns'] = ("CID","CName")
custom_font =('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg="white",font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#format column
my_tree.column('#0',width=0,stretch='no')
my_tree.column('CID',width=100,anchor=CENTER)
my_tree.column('CName',width=300,anchor=W)
#create heading
my_tree.heading('CID',text="ID",anchor=CENTER)
my_tree.heading('CName',text="Course Name",anchor=CENTER)

my_tree.place(x=30,y=250)

# add save,exit and reset button
savebtn = Button(frame,
                text="Save",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'))
savebtn.place(x=330,y=430)

exitbtn = Button(frame,
                text="Exit",
                border=0,
                bg="white",
                fg='#000000',
                cursor='hand2',
                font=('Microsoft YaHei UI Light',8),
                width=10,
                height=0,command=exitwindow)
exitbtn.place(x=350,y=465)


root.mainloop()