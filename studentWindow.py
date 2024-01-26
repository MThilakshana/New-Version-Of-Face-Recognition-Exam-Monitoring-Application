from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import subprocess

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

#define exit button
def exitwin():
    result = messagebox.askyesno("Confirmation","Do you want to exit?")
    if result:
        root.destroy()

root=Tk()
root.title('Student Dashboard - LearnMaster 1.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#define frames
blueframe = Frame(root,
                  width=200,
                  height=500,
                  bg="#57a1f8")
blueframe.place(x=0,y=0)

mainframe = Frame(root,
                 width=725,
                 height=500)
mainframe.place(x=200,y=0)

logoframe = Frame(mainframe,
                  width=725,
                  height=65,
                  bg="#57a1f8")
logoframe.place(x=0,y=0)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/logo.png')
Label(blueframe,
      image=img,
      bg="#57a1f8").place(x=50,y=5)

#make blue frame
joinclass = Button(blueframe,
                      text="Join Class",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w')
joinclass.place(x=5,y=80)

joinexam = Button(blueframe,
                      text="Join Exam",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w')
joinexam.place(x=5,y=120)

exit = Button(blueframe,
                      text="Exit",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=exitwin)
exit.place(x=5,y=460)


#add label
Label(mainframe,
      text="Dashboard - LearnMaster 1.0",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="#57a1f8",
      fg="White",
      width=45,
      anchor='center').place(x=0,y=10)








root.mainloop()