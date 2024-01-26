from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)

#check password
def login():
    try:
        cursor = mydb.cursor()
        sql = "SELECT Password FROM studentdetails WHERE Uname = %s"
        record = user.get()
        cursor.execute(sql,(record,))
        result = cursor.fetchone()
        password = result[0]

        #check password
        if(password==code.get()):
            studentWindow()
        else:
            messagebox.showinfo("Warning", "Incorrect Password or Username")
        cursor.close()
    except:
        messagebox.showinfo("Warning", "Invalid Username") 

#open register window 
def registerWindow():
    root.destroy()
    p_result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/RegistrationWindow.py'], check=True)
    
#open student window
def studentWindow():
    root.destroy()
    p_result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentWindow.py'], check=True)

root=Tk()
root.title('Login as Student - LearnMaster 1.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/login.png')
Label(root,
      image=img,
      bg='White').place(x=50,y=50)

frame = Frame(root,
              width=350,
              height=350,
              bg="white")
frame.place(x=480,y=70)

heading = Label(frame,
                text='Sign in',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=100,y=5)

#add entry box for user name
def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

#add underline for entry box
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=107)

#add entry box for password
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
        
code = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=177)

#add button
Button(frame,
       width=39,
       pady=7,
       text='Sign in',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       command=login).place(x=35,y=204)

label = Label(frame,
              text="Don't have an account?",
              fg='black',
              bg='white',
              font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

signup = Button(frame,
                text='Sign up',
                border=0,
                bg='white',
                cursor='hand2',
                fg='#57a1f8',
                command=registerWindow)
signup.place(x=215,y=270)


root.mainloop()