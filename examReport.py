from tkinter import *

root = Tk()
root.geometry('700x700')
root.title('Exam Report - LearnMaster 1.0')
root.resizable(False,False)
root.configure(bg="#fff")

Label(root,
      text="Exam Report",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="white",
      fg="#57a1f8").pack(fill=X,pady=10)

framelabel= Frame(root,
                  width=700,
                  height=50,
                  bg='green').pack(fill=X)

frameTable = Frame(root,
                   width=700,
                   height=530,
                   bg='red').pack(fill=X)

Label(framelabel,
      text="Exam ID",
      font=('Microsoft YaHei UI Light',13),
      fg='black',
      bg='white').place(x=10,y=20)

eid = Entry(framelabel,
            font=('Microsoft YaHei UI Light',13),
            )

root.mainloop()