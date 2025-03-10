import subprocess
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
import pyrebase

def pass_stuid_examid():
    examid = exmid.get()
    studid = stuid.get()
    return examid,studid

def joinexambtn():
    if(exmid.get=="Exam ID" or stuid.get()=="Student ID"):
        messagebox.showinfo("Warning","All field required!")
    else:
        exam_id = exmid.get()
        student_id = stuid.get()
        file_name = exam_id+"_"+student_id
        exampath = str(exam_id)
        stupath = str(student_id)
        
        readdata = database.child("SheduleExam").child(exam_id).get().val()
        
        if(readdata==None):
            messagebox.showinfo("Warning","Invalid Exam ID or Student ID")
        else:
            path = str(exam_id+"_"+student_id)
            savedata = {"StudentID":student_id,"ExamID":exam_id}
            database.child("Finished_Exam").child(exampath).child(stupath).set(savedata)
            root.iconify() #minimize tab
            messagebox.showinfo("Message from TEST mode","Press ESC button after finish the exam!")
            
            try:
                result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/realTimeImage.py'], check=True)
                root.destroy()
                
            except subprocess.CalledProcessError as e:
                print("error fount - ", e)

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
root.title('Join To Exams - LearnMaster 2.0')
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
                text='Join To Exam',
                fg='#57a1f8',
                bg='white',
                font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=45,y=0)

#entry box for class name
def on_enter(e):
    exmid.delete(0,'end')
    
def on_leave(e):
    name1=exmid.get()
    if name1=='':
        exmid.insert(0,'Exam ID')
        
exmid = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
exmid.place(x=30,y=75)
exmid.insert(0,'Exam ID')
exmid.bind('<FocusIn>',on_enter)
exmid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=102)

#add date chooser
def on_leave(e):
    id = stuid.get()
    if id=='':
        stuid.insert(0,'Student ID')
        
def on_enter(e):
    stuid.delete(0,'end')
   
stuid = Entry(frame,
             width=30,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
stuid.place(x=30,y=145)
stuid.insert(0,'Student ID')
stuid.bind('<FocusIn>',on_enter)
stuid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=25,y=172)

#save button
Button(frame,
       width=30,
       pady=7,
       text='Join Exam',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       command=joinexambtn).place(x=45,y=200)

Label(frame,
      text='After join the class this application will capture image\nusing your web camera.',
      bg='white',
      fg='black',
      font=('Microsoft YaHei UI Light',9)).place(x=0,y=240)

root.mainloop()