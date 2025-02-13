from tkinter import *
from tkinter import messagebox
import subprocess
import pyrebase

#check password
def login():
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
    password = code.get()
    
    students = database.child("StudentDetails").get()
    
    password_found = False
        
    if students.each():
        for student in students.each():
            student_data = student.val()
            if 'username' in student_data and student_data['username'] == username:
                if student_data['password'] == password:
                    password_found = True
                    studentWindow()
                else:
                    messagebox.showinfo("Warning","Invalid Password!")
    
    if password_found == False:
        messagebox.showinfo("Warning","Invalid Username!")


#open register window 
def registerWindow():
    root.destroy()
    p_result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/RegistrationWindow.py'], check=True)
    
#open student window
def studentWindow():
    root.destroy()
    p_result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentWindow.py'], check=True)

root=Tk()
root.title('Login as Student - LearnMaster 2.0')
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
def on_enter_password(e):
    # Clear the password field when focused
    if code.get() == 'Password':
        code.delete(0, 'end')  # Clear the field
    code.config(show='*')  # Mask the input as asterisks

def on_leave_password(e):
    # Restore the placeholder if the field is empty
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(show='')  # Show plain text for the placeholder
    else:
        code.config(show='*')  # Keep showing asterisks if not empty

code = Entry(frame,
             width=25,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')  # Set initial placeholder text
code.bind('<FocusIn>', on_enter_password)  # Handle focus in
code.bind('<FocusOut>', on_leave_password)  # Handle focus out

Frame(frame,
      width=295,
      height=2,
      bg='black').place(x=25, y=177)

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