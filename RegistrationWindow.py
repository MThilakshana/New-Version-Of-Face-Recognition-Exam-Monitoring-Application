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

def signinWin():
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentlogin.py'], check=True)

#save data
def saveData():
    #check all feild filled or not
    if(name.get()=="Name" or email.get()=="Email" or user.get()=="Username" or password.get()=="Password" or repassword.get()=="Confirm Password"):
        messagebox.showinfo("Message", "All field required")
        
    #confirm password eqaul or not
    elif(password.get()!=repassword.get()):
        messagebox.showinfo("Message", "Password doesn't match")
        
    else:
        cursor = mydb.cursor()
                
        nameV = name.get()
        emailV = email.get()
        userV = user.get()
        passwordV = password.get()
        
        #check user name availble or not
        sql = "SELECT Uname FROM studentdetails WHERE Uname= %s"
        record = userV
        cursor.execute(sql,(record,))
        result = cursor.fetchone()
        
        if result is not None:
            messagebox.showinfo("Message", "Username already taken")
        else:
            #genarate sid
            cursor.execute("SELECT COUNT(*) FROM studentdetails")
            rowCount = cursor.fetchone()[0]
            id = rowCount + 1
            
            #save data
            cursor.execute("INSERT INTO studentdetails VALUES(%s,%s,%s,%s,%s)",(id,nameV,emailV,userV,passwordV))
            mydb.commit()
            messagebox.showinfo("Message", "Data Saved Successfully")
            root.destroy()
            signinWin()
        
        cursor.close()


root=Tk()
root.title('Student Registation - LearnMaster 1.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/signup.png')
Label(root,
      image=img,
      bg="white").place(x=0,y=50)

frame = Frame(root,
              width=350,
              height=500,
              bg="white")
frame.place(x=480,y=5)

heading = Label(frame,
                text='Sign up',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=110,y=0)

#entry box for name
def on_enter(e):
    name.delete(0,'end')
    
def on_leave(e):
    name1=name.get()
    if name1=='':
        name.insert(0,'Name')
        
name = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
name.place(x=30,y=75)
name.insert(0,'Name')
name.bind('<FocusIn>',on_enter)
name.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=102)

#entry box for email
def on_enter(e):
    email.delete(0,'end')
    
def on_leave(e):
    name=email.get()
    if name=='':
        email.insert(0,'Email')
        
email = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
email.place(x=30,y=145)
email.insert(0,'Email')
email.bind('<FocusIn>',on_enter)
email.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=172)

#entry box for username
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
user.place(x=30,y=215)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=242)

#entry box for password
def on_enter(e):
    password.delete(0,'end')
    
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0,'Password')
        
password = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
password.place(x=30,y=285)
password.insert(0,'Password')
password.bind('<FocusIn>',on_enter)
password.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=312)

#entry box for re-password
def on_enter(e):
    repassword.delete(0,'end')
    
def on_leave(e):
    name=repassword.get()
    if name=='':
        repassword.insert(0,'Confirm Password')
        
repassword = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
repassword.place(x=30,y=355)
repassword.insert(0,'Confirm Password')
repassword.bind('<FocusIn>',on_enter)
repassword.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25,y=382)

#add button
Button(frame,
       width=39,
       pady=7,
       text='Sign up',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       command=saveData).place(x=35,y=409)

label = Label(frame,
              text="Do you have an account?",
              fg='black',
              bg='white',
              font=('Microsoft YaHei UI Light',9))
label.place(x=70,y=455)

signup = Button(frame,
                text='Sign in',
                border=0,
                bg='white',
                cursor='hand2',
                fg='#57a1f8',
                command=signinWin)
signup.place(x=220,y=455)

root.mainloop()