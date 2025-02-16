from tkinter import *
from tkinter import messagebox
import pyrebase

#load data 
def loaddata():
    class_id = cid.get()
    classes_ref = database.child('Class')
    class_data = classes_ref.get().val()
    
    for class_key, class_info in class_data.items():
        if class_info.get("classid") == class_id:
            cname.delete(0,END)
            cname.insert(0,class_info.get("classname"))
            cdate.delete(0,END)
            cdate.insert(0,class_info.get("startdate"))
            break

'''
#delete data
def deleteData():
    sql = "DELETE FROM classdetails WHERE CID = %s"
    record = cid.get()
    cursor.execute(sql,(record,))
    mydb.commit()
    messagebox.showinfo("Message","Data Deleted Successfully!")
    root.destroy()'''
    
#update data
def updateData():
    class_id = cid.get()
    class_ref = database.child('Class')
    class_data = class_ref.get().val()
    
    for class_key,class_info in class_data.items():
        if class_info.get("classid") == class_id:
            data_to_save = {"classid":cid.get(),"classname":cname.get(),"startdate":cdate.get()}
            database.child("Class").child(class_id).set(data_to_save)
            messagebox.showinfo("Message","Data Updated Successfully!")
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
root.title('Edit Class Details - LearnMaster 2.0')
root.geometry('925x350+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

label = Label(root,
              text="Edit Class Details",
              fg='#57a1f8',
              bg='white',
              font=('Microsoft YaHei UI Light',25,'bold'))
label.place(x=105,y=0)

#add cid label and entry box
cidlabel = Label(root,
                 text="Class ID",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
cidlabel.place(x=10,y=70)

cid = Entry(root,
            width=30,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
cid.place(x=115,y=70)

Frame(root,
      width=250,
      height=2,
      bg='black').place(x=115,y=100)

#add cname label and entry box
cnamelabel = Label(root,
                 text="Class Name",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
cnamelabel.place(x=10,y=140)

cname = Entry(root,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
cname.place(x=115,y=140)

Frame(root,
      width=370,
      height=2,
      bg='black').place(x=115,y=170)

#add cdate label and entry box
cdatelabel = Label(root,
                 text="Class Date",
                 font=('Microsoft YaHei UI Light',11),
                 fg='Black',
                 bg='White')
cdatelabel.place(x=10,y=210)

cdate = Entry(root,
            width=45,
            border=0,
            bg="white",
            font=('Microsoft YaHei UI Light',11),
            fg="black")
cdate.place(x=115,y=210)

Frame(root,
      width=370,
      height=2,
      bg='black').place(x=115,y=240)

#load button
addbtn = Button(root,
                text="Load",
                font=('Microsoft YaHei UI Light',11, 'bold'),
                width=10,
                height=0,
                bg='#57a1f8',
                border=0,
                pady=2,
                fg='White',
                cursor='hand2',
                command=loaddata)
addbtn.place(x=380,y=70)

#update button
updatebtn = Button(root,
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
deletebtn = Button(root,
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
extbtn = Button(root,
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
img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/editexam.png')
Label(root,
      image=img,
      bg='white').place(x=490,y=80)

root.mainloop()