from tkinter import *
import mysql.connector

def endclassbutton():
    x = 0

def assignvalue(cid,sid):
    class_id = cid
    student_id = sid
    
    root=Tk()
    root.title('End Class - LearnMaster 1.0')
    root.geometry('300x180+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    cidText = "Class ID - "+class_id
    sidText = "Student ID - "+student_id
    
    Label(root,
        text=cidText,
        font=('Microsoft YaHei UI Light',12, 'bold'),
        bg="white",
        fg='black').pack(fill=X,pady=20)
    
    Label(root,
        text=sidText,
        font=('Microsoft YaHei UI Light',12, 'bold'),
        bg="white",
        fg='black').pack(fill=X)
    
    #add button
    endbtn = Button(root,
                    width=30,
                    pady=7,
                    text='End Class',
                    bg="#57a1f8",
                    fg='white',
                    border=0,
                    cursor='hand2',
                    command=endclassbutton)
    endbtn.pack(fill=X,pady=20,padx=40)

    root.mainloop()

