from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import subprocess
import pyrebase

#define startExam button
def startclasswindow():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/startCls.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)

#define startExam button
def startexamwindow():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/startExam.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)

#define exit button
def exitwin():
    result = messagebox.askyesno("Confirmation","Do you want to exit?")
    if result:
        root.destroy()
        
#open editExam window
def openeditExam():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/editExam.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)
 
#open editStudent Window
def openeditStudent():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/editStudent.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)
     
#open addClass Window
def openaddClass():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/addClass.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)

#open editclass Window
def openeditClass():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/editClass.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)
    
#open addStudent Window
def openaddStudent():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/addStudent.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)

#open addStudent Window
def openexamshedule():
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/sheduleExam.py'], check=True)
      root.destroy()
      result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminWindow.py'], check=True)

def addDataToStudentTable():
      student_data = {}
      students = database.child("StudentDetails").get()
      
      for student in students.each():
            student_id = student.key()
            student_details = student.val()
            student_data[student_id] = student_details
            
      # add data to the table
      count = 0
      for student_id,details in student_data.items():
            if count == 0: # to skip first data row
                  count = count + 1 
                  continue 
            name = details.get("name","N/A")
            email = details.get("email","N/A")
            my_tree.insert("","end",values=(student_id,name,email))
            
def addDataToClassTable():
      class_data = {}
      classes = database.child("Class").get()
      
      for classv in classes.each():
            class_id = classv.key()
            class_details = classv.val()
            class_data[class_id] = class_details
            
      count = 0
      for class_id,details in class_data.items():
            if count == 0:
                  count = count + 1
                  continue
            classid = details.get("classid","N/A")
            classname = details.get("classname","N/A")
            startdate = details.get("startdate","N/A")
            class_tree.insert("",'end',values=(classid,classname,startdate))
            
def addDataToExamTable():
      exam_data = {}
      exams = database.child("SheduleExam").get()
      
      for exam in exams.each():
            exam_id = exam.key()
            exam_Details = exam.val()
            exam_data[exam_id] = exam_Details
            
      for exam_id,details in exam_data.items():
            name = details.get("examname")
            date = details.get("examdate")
            exam_tree.insert("","end",values=(exam_id,name,date))
        
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
root.title('Admin Dashboard - LearnMaster 2.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#define frames
blueframe = Frame(root,
                  width=200,
                  height=500,
                  bg="#57a1f8")
blueframe.place(x=0,y=0)

mainframe = Frame(root,
                 width=725,
                 height=500)
mainframe.place(x=200,y=0)

logoframe = Frame(mainframe,
                  width=725,
                  height=65,
                  bg="#57a1f8")
logoframe.place(x=0,y=0)

studentlist = Frame(mainframe,
                       width=450,
                       height=435,)
studentlist.place(x=0,y=65)

classlist = Frame(mainframe,
                       width=275,
                       height=230)
classlist.place(x=450,y=65)

examlist = Frame(mainframe,
                       width=275,
                       height=205)
examlist.place(x=450,y=295)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/logo.png')
Label(blueframe,
      image=img,
      bg="#57a1f8").place(x=50,y=5)

#make blue frame
startlecture = Button(blueframe,
                      text="Start Class",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=startclasswindow)
startlecture.place(x=5,y=80)

addnewclass = Button(blueframe,
                      text="Add New Class",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openaddClass)
addnewclass.place(x=5,y=120)

addnewstudent = Button(blueframe,
                      text="Students To Class",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openaddStudent)
addnewstudent.place(x=5,y=160)

shedulexam = Button(blueframe,
                      text="Shedule Exam",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openexamshedule)
shedulexam.place(x=5,y=200)

editlecutre = Button(blueframe,
                      text="Edit Class Details",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openeditClass)
editlecutre.place(x=5,y=240)

editstudent = Button(blueframe,
                      text="Edit Student Details",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openeditStudent)
editstudent.place(x=5,y=280)

editexam = Button(blueframe,
                      text="Edit Exam Details",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=openeditExam)
editexam.place(x=5,y=320)

startExam = Button(blueframe,
                      text="Start Exam",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=startexamwindow)
startExam.place(x=5,y=360)

seeexamdetails = Button(blueframe,
                      text="Show Exam Details",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w')
seeexamdetails.place(x=5,y=400)

exit = Button(blueframe,
                      text="Exit",
                      border=0,
                      bg="#57a1f8",
                      fg='white',
                      cursor="hand2",
                      width=22,
                      font=('Microsoft YaHei UI Light',13,'bold'),
                      anchor='w',
                      command=exitwin)
exit.place(x=5,y=460)

#add label
Label(mainframe,
      text="Dashboard - LearnMaster 2.0",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="#57a1f8",
      fg="White",
      width=45,
      anchor='center').place(x=0,y=10)

#labels for table tipoc
studentDetailsLabel = Label(studentlist,
                            text="Student List",
                            font=('Microsoft YaHei UI Light',12,'bold'),
                            fg='#57a1f8')
studentDetailsLabel.place(x=10,y=0)

classDetailsLabel = Label(classlist,
                            text="Class List",
                            font=('Microsoft YaHei UI Light',12,'bold'),
                            fg='#57a1f8')
classDetailsLabel.place(x=10,y=0)

examDetailsLabel = Label(examlist,
                            text="Exam List",
                            font=('Microsoft YaHei UI Light',12,'bold'),
                            fg='#57a1f8')
examDetailsLabel.place(x=10,y=0)


#add student table
my_tree = ttk.Treeview(studentlist,height=18)
my_tree['columns'] = ("SID","Name","Email")
custom_font = ('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg='#57a1f8',font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#foramt column
my_tree.column('#0',width=0, stretch='no')
my_tree.column('SID',width=50,anchor=CENTER)
my_tree.column('Name',width=200,anchor=W)
my_tree.column('Email',width=180,anchor=W)
#create headding
my_tree.heading('SID',text='SID',anchor=CENTER)
my_tree.heading('Name',text='Name',anchor=CENTER)
my_tree.heading('Email',text='Email',anchor=CENTER)

addDataToStudentTable()

my_tree.place(x=10,y=30)

#add class table
class_tree = ttk.Treeview(classlist,height=8)
class_tree['columns'] = ("CID","Class","Date")
class_tree.tag_configure('custom_font',font=custom_font)

class_tree.column('#0',width=0,stretch='no')
class_tree.column('CID',width=50,anchor=CENTER)
class_tree.column('Class',width=150,anchor=W)
class_tree.column('Date',width=50,anchor=W)

class_tree.heading('CID',text='CID',anchor=CENTER)
class_tree.heading('Class',text='Class',anchor=CENTER)
class_tree.heading('Date',text='Date',anchor=CENTER)

addDataToClassTable()

class_tree.place(x=10,y=30)

#add exam table
exam_tree = ttk.Treeview(examlist,height=6)
exam_tree['columns'] = ("EID","Exam","Date")
exam_tree.tag_configure('custom_font',font=custom_font)

exam_tree.column('#0',width=0,stretch='no')
exam_tree.column('EID',width=50,anchor=CENTER)
exam_tree.column('Exam',width=150,anchor=W)
exam_tree.column('Date',width=50,anchor=W)

exam_tree.heading('EID',text='EID',anchor=CENTER)
exam_tree.heading('Exam',text='Exam',anchor=CENTER)
exam_tree.heading('Date',text='Date',anchor=CENTER)

addDataToExamTable()

exam_tree.place(x=10,y=40)

root.mainloop()