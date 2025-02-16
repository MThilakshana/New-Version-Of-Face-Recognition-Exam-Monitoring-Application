from tkinter import *
from tkinter import messagebox
import mysql.connector
import pyrebase

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

#load function
def loadData():
    sidval = sid.get()
    if sidval != "":
        students_ref = database.child('StudentDetails').child(sidval)
        student_data = students_ref.get().val()
        
        if student_data:
            sname.insert(0,student_data.get('name'))
            email.insert(0,student_data.get('email'))
        else:
            messagebox.showinfo("Warning","Invalid Student ID!")
    else:
        messagebox.showinfo("Warning","Enter Student ID!")
    
        
#update function
def updateData():
    stuid = sid.get()
    stuname = sname.get()
    semail = email.get()
    
    if (stuid != "" or stuname != "" or  semail != ""):
        data_to_save = {"name":stuname,"email":semail}
        database.child("StudentDetails").child(stuid).update(data_to_save)
        messagebox.showinfo("Message","Data Updated Successfully!")
        root.destroy()
    else:
        messagebox.showinfo("Warning","All filed required!")
        
'''    
#delete function
def deleteData():
    sql = "DELETE FROM students WHERE SID = %s"
    record = sid.get()
    cursor.execute(sql,(record,))
    mydb.commit()
    messagebox.showinfo("Message","Data Deleted Successfully!")
    root.destroy()'''
    
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

root=Tk()
root.title('Edit Student Details - LearnMaster 1.0')
root.geometry('835x330+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

frame = Frame(root,
              width=500,
              height=350,
              bg='white')
frame.place(x=335,y=0)

label = Label(frame,
              text="Edit Student Details",
              fg='#57a1f8',
              bg='white',
              font=('Microsoft YaHei UI Light',25,'bold'))
label.place(x=90,y=0)

#add sid label and entry box
sidlabel = Label(frame,
                 text="Student ID",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
sidlabel.place(x=10,y=70)

sid = Entry(frame,
            width=30,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
sid.place(x=115,y=70)

Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=115,y=100)

#add name label and entry box
snamelabel = Label(frame,
                 text="Name",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
snamelabel.place(x=10,y=140)

sname = Entry(frame,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
sname.place(x=115,y=140)

Frame(frame,
      width=370,
      height=2,
      bg='black').place(x=115,y=170)

#add email label and entry box
emaillabel = Label(frame,
                 text="Email",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
emaillabel.place(x=10,y=210)

email = Entry(frame,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
email.place(x=115,y=210)

Frame(frame,
      width=370,
      height=2,
      bg='black').place(x=115,y=240)

#load button
addbtn = Button(frame,
                text="Load",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2',
                command=loadData)
addbtn.place(x=380,y=70)

#update button
updatebtn = Button(frame,
                text="Update",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2',
                command=updateData)
updatebtn.place(x=380,y=280)

#delete button
deletebtn = Button(frame,
                text="Delete",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2')
deletebtn.place(x=250,y=280)

#edit button
extbtn = Button(frame,
                text="Exit",
                font=('Microsoft YaHei UI Light',10),
                width=10,
                height=0,
                bg='white',
                border=0,
                pady=2,
                fg='black',
                cursor='hand2',
                anchor=W,
                command=root.destroy)
extbtn.place(x=10,y=280)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/editstu.png')
Label(root,
      image=img,
      bg='white').place(x=50,y=50)

root.mainloop()