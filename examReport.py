from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x700')
root.title('Exam Report - LearnMaster 1.0')
root.resizable(False,False)
root.configure(bg="#fff")

mainlabel = Frame(root,
                  width=700,
                  height=70,
                  bg='white')
mainlabel.pack(fill=X)

framelabel= Frame(root,
                  width=700,
                  height=50,
                  bg='white')
framelabel.pack(fill=X)

frameTable = Frame(root,
                   width=700,
                   height=530,
                   bg='white')
frameTable.pack(fill=X)

framebottom = Frame(root,
                    width=700,
                    height=50,
                    bg='red')
framebottom.pack(fill=X)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/logo.png')
Label(mainlabel,
      image=img,
      bg="white").place(x=590,y=5)

Label(mainlabel,
      text="Exam Report",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="white",
      fg="#57a1f8").place(x=10,y=15)

Label(framelabel,
      text="Exam ID",
      font=('Microsoft YaHei UI Light',10,'bold'),
      fg='black',
      bg='white').place(x=10,y=10)

eid = Entry(framelabel,
            font=('Microsoft YaHei UI Light',10),
            width=30,
            border=2)
eid.place(x=100,y=10)

searchbtn = Button(framelabel,
                   text="Search",
                   font=('Microsoft YaHei UI Light',8,'bold'),
                   width=12,
                   fg='white',
                   bg='#57a1f8',
                   cursor='hand2',
                   border=0
                   )
searchbtn.place(x=600,y=10)

custom_font = ('Microsoft YaHei UI Light',10)

#add data table
my_tree = ttk.Treeview(frameTable,
                       height = 23)
my_tree['columns'] = ("Student ID","Screen Time","TAPDT","Captured APNDT","Status")
my_tree.tag_configure('custom_font',font=custom_font)

my_tree.column('#0',width=0,stretch='no')
my_tree.column('Student ID',width=100,anchor=CENTER)
my_tree.column('Screen Time',width=150,anchor=E)
my_tree.column('TAPDT',width=150,anchor=E)
my_tree.column('Captured APNDT',width=150,anchor=E)
my_tree.column('Status',width=100,anchor=CENTER)

my_tree.heading('Student ID',text='Student ID',anchor=CENTER)
my_tree.heading('Screen Time',text='Screen Time',anchor=CENTER)
my_tree.heading('TAPDT', text='TAPDT',anchor=CENTER)
my_tree.heading('Captured APNDT', text='Captured APNDT', anchor=CENTER)
my_tree.heading('Status',text='Status',anchor=CENTER)

my_tree.pack(fill=X,padx=10)

Label(frameTable,
      text='TAPDT - Total Authorized Person Detected Time\nAPNDT - Authorized Person Not Detected Time',
      font=('Microsoft YaHei UI Light',8),
      bg='white').pack(fill=X)

#button
exitbtn = Button(framebottom,
                text="Exit",
                font=('Microsoft YaHei UI Light',8,'bold'),
                width=12,
                fg='white',
                bg='#57a1f8',
                cursor='hand2',
                border=0)
exitbtn.place(x=10,y=20)

printbtn = Button(framebottom,
                text="Print",
                font=('Microsoft YaHei UI Light',8,'bold'),
                width=12,
                fg='white',
                bg='#57a1f8',
                cursor='hand2',
                border=0)
printbtn.place(x=600,y=20)

root.mainloop()