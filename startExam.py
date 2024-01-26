from tkinter import *
from tkinter import ttk
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import pyrebase

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()


#check btn function
def checkBtn():
    if(eid.get()=="Exam ID"):
        messagebox.showinfo("Warning","Enter Exam ID")
    else:
        sql = "SELECT Name,Time,Date,SID FROM examdetails WHERE EID = %s"
        record = (eid.get(),)
        cursor.execute(sql,record)
        data = cursor.fetchone()
        
        if(data==None):
            messagebox.showinfo("Warning","Invalid Exam ID!")
        else:
            examnameEntry.insert(0,data[0])
            timeEntry.insert(0,data[1])
            dateEntry.insert(0,data[2])
            sidentry.insert(0,data[3])

    
#start exam button 
def startExambtn():
    exm_id = eid.get()
    exm_name = examnameEntry.get()
    exm_subject = sidentry.get()
    exm_date = str(dateEntry.get())
    exm_time = timeEntry.get()
    
    
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
    
    savedata = {"Exam ID":exm_id,"Exam Name":exm_name,"Subject":exm_subject,"Date":exm_date,"Time":exm_time}
    
    path = exm_id+"_"+exm_subject
    #save data
    response = database.child("Exam").child(path).set(savedata)
    
    messagebox.showinfo("Message","Exam Ready to Start!")
    cursor.close()
    root.destroy()
    
      

root=Tk()
root.title('Start Lecture - LearnMaster 1.0')
root.geometry('435x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#add heading
heading = Label(root,
                text='Start Exam',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.pack(fill=X)

#entry box for exam id
def on_enter(e):
    eid.delete(0,'end')
    
def on_leave(e):
    name1=eid.get()
    if name1=='':
        eid.insert(0,'Exam ID')
        
eid = Entry(root,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
eid.place(x=30,y=75)
eid.insert(0,'Exam ID')
eid.bind('<FocusIn>',on_enter)
eid.bind('<FocusOut>', on_leave)

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
                font=('Microsoft YaHei UI Light',11, 'bold'),
                command=checkBtn)
checkbtn.place(x=300,y=70)

#exam name
examnamelb = Label(root,
                  text="Class Name",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=145)

examnameEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
examnameEntry.place(x=150,y=145)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=175)

#student id
subidlb = Label(root,
                  text="Subject ID",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=215)

sidentry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
sidentry.place(x=150,y=215)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=245)

#Date
exmdatelb = Label(root,
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

#time
exmtimelb = Label(root,
                  text="Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=355)

timeEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
timeEntry.place(x=150,y=355)

Frame(root,
     width=260,
      height=2,
      bg='black').place(x=145,y=385)




#start button
startbtn = Button(root,
                text="Start",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'),
                command=startExambtn)
startbtn.place(x=168,y=435)

#exit button
exitbtn = Button(root,
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
exitbtn.place(x=188,y=468)


root.mainloop()