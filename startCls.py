from tkinter import *
from tkinter import ttk
import datetime

root=Tk()
root.title('Start Lecture - LearnMaster 1.0')
root.geometry('775x400+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#add heading
heading = Label(root,
                text='Start Lecture',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=30,y=0)

#entry box for class id
def on_enter(e):
    cid.delete(0,'end')
    
def on_leave(e):
    name1=cid.get()
    if name1=='':
        cid.insert(0,'Class ID')
        
cid = Entry(root,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
cid.place(x=30,y=75)
cid.insert(0,'Class ID')
cid.bind('<FocusIn>',on_enter)
cid.bind('<FocusOut>', on_leave)

#add line
Frame(root,
      width=250,
      height=2,
      bg='black').place(x=25,y=102)

#check button
checkbtn = Button(root,
                text="Check",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'))
checkbtn.place(x=300,y=70)


#Class name
clsnamelb = Label(root,
                  text="Class Name",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=145)

clsnameEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
clsnameEntry.place(x=150,y=145)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=175)

#No of students
clsnamelb = Label(root,
                  text="No Of Students",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=215)

clsnameEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
clsnameEntry.place(x=150,y=215)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=245)

#Date
clsdatelb = Label(root,
                  text="Date",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=285)

dateEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
dateEntry.place(x=150,y=285)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=315)




root.mainloop()