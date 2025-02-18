from tkinter import *
from tkinter import ttk
from datetime import datetime,date
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

#check details of class
def checkBtn():
      if (cid.get()=="Class ID"):
            messagebox.showinfo("Warning","Enter Class ID")
      else:
            clsid = cid.get()
            class_data = database.child("Class").child(clsid).get().val()
            
            if class_data:
                  clsname = class_data.get('classname')
                  clsnameEntry.insert(0,clsname)
            else:
                  messagebox.showinfo("Warning","Invalid Classt ID!")

            stu_to_cls = database.child("StudentToClass").child(clsid).get().val()
            
            if stu_to_cls:
                  stu_count = len(stu_to_cls) - 1
                  stucount.insert(0,stu_count)
            else:
                  messagebox.showinfo("Warning","Students not assign yet!")
            
#send email
def sendemail(st_email):
      print('email sent')
            
            
#add function to start button
def startClass():
      class_Name = clsnameEntry.get()
      class_id = cid.get()
      class_date = dateEntry.get()
      class_time = hour_combo.get() + ":" + minute_combo.get()
      start_date = str(date.today())
      start_time = str(datetime.now().time())
      
      if class_Name=="" or stucount.get()=="":
            messagebox.showinfo("Warning","Please check the Class ID!")
      else:
            data_to_save = {"classname":class_Name,"startdate":start_date,"starttime":start_time,"studentscount":stucount.get()}
            database.child("StartClass").child(class_id).set(data_to_save)
            messagebox.showinfo("Message","Class Ready to Start!")
            root.destroy()
      
      
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
root.title('Start Lecture - LearnMaster 1.0')
root.geometry('435x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#get date
current_date = datetime.now()
formatted_date = current_date.strftime('%Y-%m-%d')

#add heading
heading = Label(root,
                text='Start Lecture',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.pack(fill=X)

#entry box for class id
def on_enter(e):
    cid.delete(0,'end')
    
def on_leave(e):
    name1=cid.get()
    if name1=='':
        cid.insert(0,'Class ID')
        
cid = Entry(root,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
cid.place(x=30,y=75)
cid.insert(0,'Class ID')
cid.bind('<FocusIn>',on_enter)
cid.bind('<FocusOut>', on_leave)

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


#Class name
clsnamelb = Label(root,
                  text="Class Name",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=145)

clsnameEntry = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
clsnameEntry.place(x=150,y=145)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=175)

#No of students
stcountlb = Label(root,
                  text="No Of Students",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=215)

stucount = Entry(root,
                    width=30,
                    fg='Black',
                    border=0,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
stucount.place(x=150,y=215)

Frame(root,
      width=260,
      height=2,
      bg='black').place(x=145,y=245)

#Date
clsdatelb = Label(root,
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

#add date to date Entry
dateEntry.insert(0,formatted_date)

Frame(root,
     width=260,
      height=2,
      bg='black').place(x=145,y=315)

#time
clstimelb = Label(root,
                  text="Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=25,y=355)

current_time = datetime.now().time()

hours = [str(i).zfill(2) for i in range(24)]
hours_var = StringVar(value=current_time.strftime("%H"))
hour_combo = ttk.Combobox(root,
                          values=hours,
                          width=5,
                          font=('Microsoft YaHei UI Light',11),
                          textvariable=hours_var)
hour_combo.place(x=150,y=355)

# Create a Combobox for minutes
minutes = [str(i).zfill(2) for i in range(60)]
minutes_var = StringVar(value=current_time.strftime("%M"))
minute_combo = ttk.Combobox(root,
                            values=minutes,
                            font=('Microsoft YaHei UI Light',11),
                            width=5,
                            textvariable=minutes_var)
minute_combo.place(x=270,y=355)

hlb = Label(root,
            text="Hours",
            font=('Microsoft YaHei UI Light',11),
            fg="black",
            bg='white').place(x=220,y=355)
mlb = Label(root,
            text="Minutes",
            font=('Microsoft YaHei UI Light',11),
            fg="black",
            bg='white').place(x=340,y=355)

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
                command=startClass)
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