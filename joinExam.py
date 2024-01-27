from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector
from tkinter import messagebox

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

def joinexambtn():
    if()

root=Tk()
root.title('Join To Exams - LearnMaster 1.0')
root.geometry('775x300+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/classSmall.png')
Label(root,
      image=img,
      bg="white").place(x=0,y=0)

frame = Frame(root,
              width=300,
              height=300,
              bg='white')
frame.place(x=450,y=0)

#add heading
heading = Label(frame,
                text='Join To Exam',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=45,y=0)

#entry box for class name
def on_enter(e):
    exmid.delete(0,'end')
    
def on_leave(e):
    name1=exmid.get()
    if name1=='':
        exmid.insert(0,'Exam ID')
        
exmid = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
exmid.place(x=30,y=75)
exmid.insert(0,'Exam ID')
exmid.bind('<FocusIn>',on_enter)
exmid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=102)

#add date chooser
def on_leave(e):
    id = stuid.get()
    if id=='':
        stuid.insert(0,'Subject ID')
        
def on_enter(e):
    stuid.delete(0,'end')
   
stuid = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
stuid.place(x=30,y=145)
stuid.insert(0,'Subject ID')
stuid.bind('<FocusIn>',on_enter)
stuid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=172)

#save button
Button(frame,
       width=30,
       pady=7,
       text='Join Exam',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2').place(x=45,y=200)

Label(frame,
      text='After join the class this application will capture image\nusing your web camera.',
      bg='white',
      fg='black',
      font=('Microsoft YaHei UI Light',9)).place(x=0,y=240)

root.mainloop()