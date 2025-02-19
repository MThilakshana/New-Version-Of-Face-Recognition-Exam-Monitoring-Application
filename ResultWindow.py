from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def getinput():
      
      def displayrep():
            stuid = userid_entry.get()
            examid = examid_entry.get()
            
            if(stuid=="" or examid==""):
                  messagebox.showinfo("Warning","All fields required!")
            else:
                  return examid,stuid
            
      window = Tk()
      window.title('Exam Report - Get Info')
      window.geometry('250x200')
      window.configure(bg="#fff")
      window.resizable(False,False)
      
      exam_id = Label(window,
                  text="Exam ID",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=20)
      
      examid_entry = Entry(window,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
      examid_entry.place(x=15,y=50)
      
      userid = Label(window,
                  text="Student ID",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=80)
      
      userid_entry = Entry(window,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
      userid_entry.place(x=15,y=110)
      
      startbtn = Button(window,
                text="Enter",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'),
                command=displayrep)
      startbtn.place(x=15,y=140)

      window.mainloop()

examid,stuid = getinput()

def showdata():
      return None

root=Tk()
root.title('Exam Report - LearnMaster 2.0')
root.geometry('700x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

logoframe = Frame(root,
                  width=725,
                  height=80,
                  bg="#57a1f8")
logoframe.place(x=0,y=0)

sideframe = Frame(root,
                  width=500,
                  height=1000,
                  bg="#fff")
sideframe.place(x=450,y=80)

#add label
Label(logoframe,
      text="Exam Report",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="#57a1f8",
      fg="White",
      width=45,
      anchor='center').place(x=0,y=20)

totscreentime = Label(sideframe,
                  text="Total Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=20)

authscreentime = Label(sideframe,
                  text="Total Authorized Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=80)

unauthscreentime = Label(sideframe,
                  text="Total Unuthorized Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=140)


#add entry box
totscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
totscreentime_entry.place(x=15,y=50)

authscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
authscreentime_entry.place(x=15,y=110)

unauthscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
unauthscreentime_entry.place(x=15,y=170)

#add button
exitbtn = Button(sideframe,
                text="Exit",
                bg="white",
                fg="black",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',8),
                command=root.destroy)
exitbtn.place(x=85,y=380)

#add result table
my_tree = ttk.Treeview(root,height=18)
my_tree['columns'] = ("no","reason","date")
custom_font = ('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg='#57a1f8',font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#foramt column
my_tree.column('#0',width=0, stretch='no')
my_tree.column('no',width=50,anchor=CENTER)
my_tree.column('reason',width=200,anchor=W)
my_tree.column('date',width=180,anchor=W)
#create headding
my_tree.heading('no',text='No',anchor=CENTER)
my_tree.heading('reason',text='Reason',anchor=CENTER)
my_tree.heading('date',text='Date and Time',anchor=CENTER)

my_tree.place(x=10,y=100)

root.mainloop()