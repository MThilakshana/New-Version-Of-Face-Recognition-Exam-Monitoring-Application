from tkinter import messagebox
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
import pyrebase

#exit button
def exitwindow():
    root.destroy()
    
#generate exam id
def genexamsid():
    exam = database.child("SheduleExam").get()
    examID = "EXM"+ str(len(exam.val())+1)
    return examID
    
#save data
def read():
    if(sid.get()=="Subject ID" or name.get()=="Exam Name" or time.get()=="Time (08:30 AM)" or examDate.get()=="Exam Date"):
        messagebox.showinfo("Warning", "All field required!")
    else:
        examID = genexamsid()
        subid = sid.get()
        ename = name.get()
        etime = time.get()
        edate = examDate.get()
        
        data_to_save = {"examid":examID,"subjectid":subid,"examname":ename,"examtime":etime,"examdate":edate}
        database.child("SheduleExam").child(examID).set(data_to_save)
        messagebox.showinfo("Message", "Data Saved Successfully!")
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
root.title('Schedule Exam - LearnMaster 2.0')
root.geometry('775x400+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#open date chooser
def open_date_chooser():
    examDate.delete(0,'end')
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

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/shedule.png')
Label(root,
      image=img,
      bg="white").place(x=50,y=40)

frame = Frame(root,
              width=300,
              height=400,
              bg='white')
frame.place(x=450,y=0)

#add heading
heading = Label(frame,
                text='Schedule Exam',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=30,y=0)

#entry box for subject id
def on_enter(e):
    sid.delete(0,'end')
    
def on_leave(e):
    name1=sid.get()
    if name1=='':
        sid.insert(0,'Subject ID')
        
sid = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
sid.place(x=30,y=75)
sid.insert(0,'Subject ID')
sid.bind('<FocusIn>',on_enter)
sid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=102)

#entry box for exam name
def on_enter(e):
    name.delete(0,'end')
    
def on_leave(e):
    name1=name.get()
    if name1=='':
        name.insert(0,'Exam Name')
        
name = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
name.place(x=30,y=145)
name.insert(0,'Exam Name')
name.bind('<FocusIn>',on_enter)
name.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=172)

#entry box for class time
def on_enter(e):
    time.delete(0,'end')
    
def on_leave(e):
    name1=time.get()
    if name1=='':
        time.insert(0,'Time (08:30 AM)')
        
time = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
time.place(x=30,y=215)
time.insert(0,'Time (08:30 AM)')
time.bind('<FocusIn>',on_enter)
time.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=242)

#add date chooser
def on_leave(e):
    date = examDate.get()
    if date=='':
        examDate.insert(0,'Exam Date')
    else:
        examDate.insert(0,selected_date_var)
    
selected_date_var = StringVar()
    
examDate = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11),
             textvariable=selected_date_var)
examDate.place(x=30,y=285)
examDate.insert(0,'Exam Date')
examDate.bind('<Button-1>',lambda event: open_date_chooser())
examDate.bind('<FocusOut>',on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=312)

# add save,exit button
savebtn = Button(frame,
                text="Save",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'),
                command=read)
savebtn.place(x=100,y=325)

exitbtn = Button(frame,
                text="Exit",
                border=0,
                bg="white",
                fg='#000000',
                cursor='hand2',
                font=('Microsoft YaHei UI Light',8),
                width=10,
                height=0,command=exitwindow)
exitbtn.place(x=120,y=360)

root.mainloop()