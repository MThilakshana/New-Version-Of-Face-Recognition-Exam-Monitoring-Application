from tkinter import *
import mysql.connector

def endclassbutton():
    x = 0

def assignvalue(cid,sid):
    print(cid," ",sid)
    root=Tk()
    root.title('End Class - LearnMaster 1.0')
    root.geometry('300x300+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/logosmall.gif')
    Label(root,
        image=img,
        bg="white").pack(fill=X,padx=20,pady=20)

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

