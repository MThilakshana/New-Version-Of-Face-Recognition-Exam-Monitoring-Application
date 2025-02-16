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

#define join class button
def joinClass():
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/joinClass.py'], check=True)
    root.destroy()
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentWindow.py'], check=True)
    
#define join exam butoon
def joinExam():
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/joinExam.py'], check=True)
    root.destroy()
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentWindow.py'], check=True)

#define exit button
def exitwin():
    result = messagebox.askyesno("Confirmation","Do you want to exit?")
    if result:
        root.destroy()

root=Tk()
root.title('Student Dashboard - LearnMaster 2.0')
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
                      anchor='w',
                      command=joinClass)
joinclass.place(x=5,y=80)

joinexam = Button(blueframe,
                      text="Join Exam",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=joinExam)
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
      text="Dashboard - LearnMaster 2.0",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="#57a1f8",
      fg="White",
      width=45,
      anchor='center').place(x=0,y=10)

#add student table
my_tree = ttk.Treeview(mainframe,height=18)
my_tree['columns'] = ("CID","Date","Time","SID","Status")
custom_font = ('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg='#57a1f8',font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#foramt column
my_tree.column('#0',width=0, stretch='no')
my_tree.column('CID',width=140,anchor=CENTER)
my_tree.column('Date',width=140,anchor=W)
my_tree.column('Time',width=140,anchor=W)
my_tree.column('SID',width=140,anchor=W)
my_tree.column('Status',width=140,anchor=W)
#create headding
my_tree.heading('CID',text='CID',anchor=CENTER)
my_tree.heading('Date',text='Date',anchor=CENTER)
my_tree.heading('Time',text='Time',anchor=CENTER)
my_tree.heading('SID',text='SID',anchor=CENTER)
my_tree.heading('Status',text='Status',anchor=CENTER)

my_tree.place(x=10,y=100)

#label for table tipoc
classdetaillabel = Label(mainframe,
                            text="Participated Class List",
                            font=('Microsoft YaHei UI Light',12,'bold'),
                            fg='#57a1f8')
classdetaillabel.place(x=10,y=70)

root.mainloop()