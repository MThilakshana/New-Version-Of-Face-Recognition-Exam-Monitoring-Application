from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyrebase

#exit window
def exitwindow():
    root.destroy()

# check class
def checkClass():
    if cid.get() == "Class ID":
        messagebox.showinfo("Warinig","Enter Class ID")
    else:
        class_brances = database.child("Class").get()
        
        cval = False
        
        if class_brances.val():
            for branch_id, class_data in class_brances.val().items():
                if class_data.get('classid') == cid.get():
                    class_name = class_data.get('classname')
                    cname.delete(0, END)
                    cname.insert(END, class_name)
                    cval = True
                    break
            if cval == False:
                messagebox.showinfo("Warinig","Invalid Class ID")
    
#add data to table
def addData():
    subject = dropdown.get()
    student_ref = database.child("StudentDetails")
    students = student_ref.get().val()
    
    for student_key,student_data in students.items():
        if student_data.get('name') == dropdown.get():
            my_tree.insert('','end',values=(student_key,dropdown.get()))
    
#save data in database
def read():
    if(cid.get()=="Class ID" or cname.get()=="CLass Name"):
        messagebox.showinfo("Warning","Enter Class ID and Chek It!")
    else:
        allItem = my_tree.get_children()
        count = 0
        for item in allItem:
            count = count + 1
            values = my_tree.item(item,'values')
            Data_To_Save = {count:values[0]}
            response = database.child("StudentToClass").child(cid.get()).update(Data_To_Save)
        messagebox.showinfo("Message","Data Saved Successfully")
        root.destroy()

data =  []

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

# add data to dropdown box
student_ref = database.child("StudentDetails")
student_data = student_ref.get()

if student_data.each():
    for student in student_data.each():
        student_id = student.key()
        student_name = student.val().get('name')
        
        if student_name:
            data.append((student_id,student_name))

root=Tk()
root.title('Students To Class - LearnMaster 2.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

#add image
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/stregisterSmall.png')
Label(root,
      image=img,
      bg='white').place(x=90,y=80)

#add frame for form
frame = Frame(root,
              width=450,
              height=500,
              bg='white')
frame.place(x=450,y=5)

#add label
label = Label(frame,
              text="Students To Class",
              fg='#57a1f8',
              bg='white',
              font=('Microsoft YaHei UI Light',25,'bold'))
label.place(x=95,y=0)

#entry box for name
def on_enter(e):
    cid.delete(0,'end')
    
def on_leave(e):
    name1=cid.get()
    if name1=='':
        cid.insert(0,'Class ID')
        
cid = Entry(frame,
             width=50,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
cid.place(x=30,y=75)
cid.insert(0,'Class ID')
cid.bind('<FocusIn>',on_enter)
cid.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=270,
      height=2,
      bg='black').place(x=25,y=102)

#entry box for cname
def on_enter(e):
    cname.delete(0,'end')
    
def on_leave(e):
    name=cname.get()
    if name=='':
        cname.insert(0,'Class Name')
        
cname = Entry(frame,
             width=50,
             fg='Black',
             border=0,
             bg='White',
             font=('Microsoft YaHei UI Light',11))
cname.place(x=30,y=145)
cname.insert(0,'Class Name')
cname.bind('<FocusIn>',on_enter)
cname.bind('<FocusOut>', on_leave)

#add line
Frame(frame,
      width=410,
      height=2,
      bg='black').place(x=25,y=172)

#add drop box
def on_select(e):
    selectedItem = dropdown.get()
    
selectedItem = StringVar()

dropdown = ttk.Combobox(frame,
                        textvariable=selectedItem,
                        state="readonly",
                        font=('Microsoft YaHei UI Light',11),
                        width=30)
dropdown['values'] = [item[1] for item in data]
dropdown.set("Select Student")
dropdown.place(x=30,y=215)
dropdown.bind('<<ComboboxSelected>>',on_select)

#add button
addbtn = Button(frame,
                text="Add",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2',
                command=addData)
addbtn.place(x=330,y=207)

#check button
checkbtn = Button(frame,
                text="Check",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2',
                command=checkClass)
checkbtn.place(x=330,y=75)

#add table
my_tree = ttk.Treeview(frame,height=6)
my_tree['columns'] = ("CID","CName")
custom_font =('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg="white",font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#format column
my_tree.column('#0',width=0,stretch='no')
my_tree.column('CID',width=100,anchor=CENTER)
my_tree.column('CName',width=300,anchor=W)
#create heading
my_tree.heading('CID',text="ID",anchor=CENTER)
my_tree.heading('CName',text="Student Name",anchor=CENTER)

my_tree.place(x=30,y=250)

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
savebtn.place(x=330,y=430)

exitbtn = Button(frame,
                text="Exit",
                border=0,
                bg="white",
                fg='#000000',
                cursor='hand2',
                font=('Microsoft YaHei UI Light',8),
                width=10,
                height=0,command=exitwindow)
exitbtn.place(x=350,y=465)

root.mainloop()