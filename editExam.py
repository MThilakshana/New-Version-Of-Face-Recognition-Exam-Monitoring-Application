from tkinter import *
from tkinter import messagebox
import pyrebase

#load function
def loadData():
    if eid.get() != "":
        exid = eid.get()
        exam_ref = database.child("SheduleExam").child(exid)
        exam_data = exam_ref.get().val()
        
        if exam_data:
            ename.insert(0,exam_data.get('examname'))
            edate.insert(0,exam_data.get('examdate'))
            etime.insert(0,exam_data.get('examtime'))
        else:
            messagebox.showinfo("Warning","Invalid Exam ID!")
    else:
        messagebox.showinfo("Warning","Enter Exam ID!")
    
    
#update function
def updateData():
    examid = eid.get()
    examname = ename.get()
    examtime = etime.get()
    examdate = edate.get()
    
    if (examdate != "" or examid != "" or examname != "" or examtime != ""):
        data_to_save = {"examname":examname,"examdate":examdate,"examtime":examtime}
        database.child("SheduleExam").child(examid).update(data_to_save)
        messagebox.showinfo("Message","Data Updated Successfully!")
        root.destroy()
    else:
        messagebox.showinfo("Warning","All filed required!")
    
'''
#delete function
def deleteData():
    record = eid.get()
    sql = "DELETE FROM examdetails WHERE EID=%s"
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
root.title('Edit Exam Details - LearnMaster 2.0')
root.geometry('885x380+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

frame = Frame(root,
              width=500,
              height=380,
              bg='white')
frame.place(x=385,y=0)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/exam.png')
Label(root,
      image=img,
      bg='white').place(x=0,y=70)

label = Label(frame,
              text="Edit Exam Details",
              fg='#57a1f8',
              bg='white',
              font=('Microsoft YaHei UI Light',25,'bold'))
label.place(x=125,y=0)

#add eid label and entry box
eidlabel = Label(frame,
                 text="Exam ID",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
eidlabel.place(x=10,y=70)

eid = Entry(frame,
            width=30,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
eid.place(x=115,y=70)

Frame(frame,
      width=250,
      height=2,
      bg='black').place(x=115,y=100)

#add name label and entry box
enamelabel = Label(frame,
                 text="Name",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
enamelabel.place(x=10,y=140)

ename = Entry(frame,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
ename.place(x=115,y=140)

Frame(frame,
      width=370,
      height=2,
      bg='black').place(x=115,y=170)

#add date label and entry box
edatelabel = Label(frame,
                 text="Date",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
edatelabel.place(x=10,y=210)

edate = Entry(frame,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
edate.place(x=115,y=210)

Frame(frame,
      width=370,
      height=2,
      bg='black').place(x=115,y=240)

#add Time label and entry box
etimelabel = Label(frame,
                 text="Time",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
etimelabel.place(x=10,y=280)

etime = Entry(frame,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
etime.place(x=115,y=280)

Frame(frame,
      width=370,
      height=2,
      bg='black').place(x=115,y=310)

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
updatebtn.place(x=380,y=330)

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
deletebtn.place(x=250,y=330)

#exit button
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
extbtn.place(x=10,y=330)

root.mainloop()