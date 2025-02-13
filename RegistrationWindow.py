from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
import pyrebase

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)

#create tables
cursor = mydb.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS studentdetails(id TEXT,name TEXT,email TEXT,uname TEXT,password TEXT)")

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
        #connect to the Firebase
        config = {
                "apiKey": "AIzaSyCEu0-KtmUoM6ilvpIYy6vidHnVs93aO78",
                "authDomain": "edumaster-project.firebaseapp.com",
                "projectId": "edumaster-project",
                "databaseURL": "https://edumaster-project-default-rtdb.firebaseio.com/",
                "storageBucket": "edumaster-project.appspot.com",
                "messagingSenderId": "945743272123",
                "appId": "1:945743272123:web:e64de0b72d8b7e6e26f19e",
                "measurementId": "G-XNK127X4XJ"
        }
        
        firebase = pyrebase.initialize_app(config)
        database = firebase.database()
        
        username = user.get()
        emailv = email.get()
        namev = name.get()
        pw = password.get()
        
        username_exist = False
        
        students = database.child("StudentDetails").get()
        
        if students.each():
            for student in students.each():
                student_data = student.val()
                if 'username' in student_data and student_data['username'] == username:
                    username_exist = True
                    break
                
        if username_exist:
            messagebox.showinfo("Message","Username Already Exist!")
        else:
            Data_to_save = {"email":emailv,"name":namev,"password":pw,"username":username}
            count  = len(students.val())
            path = "STU"+str(count)
            
            response = database.child("StudentDetails").child(path).set(Data_to_save)
            messagebox.showinfo("Message","User Created Successfully!")
            cursor.close()


root=Tk()
root.title('Student Registation - LearnMaster 2.0')
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
    if password.get() == 'Password':
        password.delete(0,'end')
    password.config(show='*')
    
def on_leave(e):
    if password.get() == '':
        password.insert(0,'Password')
        password.config(show='')
    else:
        password.config(show='*')
        
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
    if repassword.get() == 'Confirm Password':
        repassword.delete(0,'end')
    repassword.config(show='*')
    
def on_leave(e):
    if repassword.get() == '':
        repassword.insert(0,'Confirm Password')
        repassword.config(show='')
    else:
        repassword.config(show='*')
        
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