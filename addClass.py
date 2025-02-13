from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import mysql.connector
from tkinter import messagebox
import pyrebase

#open date chooser
def open_date_chooser():
    startDate.delete(0,'end')
    date_chooser_window = Toplevel(root)
    
    def get_selected_date():
        selected_date = cal.get_date()
        selected_date_var.set(selected_date)
        date_chooser_window.destroy()
        
    cal = Calendar(date_chooser_window,
                   selectmode='day',
                   year=2024,
                   month=1,
                   day=1)
    cal.pack(pady=20)
    
    btn_get_date = Button(date_chooser_window,
                          text='Select Date',
                          command=get_selected_date)
    btn_get_date.pack(pady=10)
    
#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)

cursor = mydb.cursor()

#save data in database
def saveData():
    if(name.get()=="Name" or startDate.get()=="Start Date"):
        messagebox.showinfo("Message","All field required")
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
        
        #generate class id
        classes = database.child("Class").get()
        count = len(classes.val())
        classid = "CID"+str(count)
        
        data_for_save ={"classid":classid,"classname":name.get(),"startdate":startDate.get()}
        response = database.child("Class").child(classid).set(data_for_save)
        messagebox.showinfo("Message","Class added Successfully!")
        root.destroy()

root=Tk()
root.title('Add New Class - LearnMaster 1.0')
root.geometry('775x300+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/classSmall.png')
Label(root,
      image=img,
      bg="white").place(x=0,y=0)

frame = Frame(root,
              width=300,
              height=300,
              bg='white')
frame.place(x=450,y=0)

#add heading
heading = Label(frame,
                text='Add New Class',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=30,y=0)

#entry box for class name
def on_enter(e):
    name.delete(0,'end')
    
def on_leave(e):
    name1=name.get()
    if name1=='':
        name.insert(0,'Class Name')
        
name = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
name.place(x=30,y=75)
name.insert(0,'Class Name')
name.bind('<FocusIn>',on_enter)
name.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=102)

#add date chooser
def on_leave(e):
    date = startDate.get()
    if date=='':
        startDate.insert(0,'Start Date')
    else:
        startDate.insert(0,selected_date_var)
    
selected_date_var = StringVar()
    
startDate = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11),
             textvariable=selected_date_var)
startDate.place(x=30,y=145)
startDate.insert(0,'Start Date')
startDate.bind('<Button-1>',lambda event: open_date_chooser())
startDate.bind('<FocusOut>',on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=172)

#save button
Button(frame,
       width=30,
       pady=7,
       text='Add Class',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       command=saveData).place(x=45,y=200)

Label(frame,
      text='Class ID will generate automatically',
      bg='white',
      fg='black',
      font=('Microsoft YaHei UI Light',9)).place(x=52,y=240)

root.mainloop()