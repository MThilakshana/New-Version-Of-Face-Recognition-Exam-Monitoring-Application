from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyrebase

def addDataToTreeView():
    examid = exid_entry.get()
    stuid = sid_entry.get()
      
    # Get the specific student's data under the given exam ID
    student_data = database.child("AuthorizedNotDetected").child(examid).child(stuid).get()

    if student_data.val():
        values = list(student_data.val().values())  # Get only values, not keys

        # Check if values exceed 3
        if len(values) > 3:
            filtered_values = values[:-3]  # Display all except the last three
        else:
            filtered_values = values  # Display all values if 3 or fewer

        # Display only the values
        for value in filtered_values:
            print(value)
    else:
        print(f"No data found for Exam ID '{examid}' and Student ID '{stuid}'.")

                  
#for det in data.each():
            
def loaddata():
      examid = exid_entry.get()
      stuid = sid_entry.get()
      
      if examid=="" or stuid=="":
            messagebox.showinfo("Warning","All field required!")
      else:
            details = database.child("Finished_Exam").child(examid).child(stuid).get().val()
      
            if details:
                  totscreentime_entry.insert(0,details.get('Total Screen Time'))
                  authscreentime_entry.insert(0,details.get('Total Authorized time'))
                  unauthscreentime_entry.insert(0,details.get('Total Unauthorized Time'))
            addDataToTreeView()
      

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
root.title('Exam Report - LearnMaster 2.0')
root.geometry('700x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

logoframe = Frame(root,
                  width=725,
                  height=80,
                  bg="#57a1f8")
logoframe.place(x=0,y=0)

sideframe = Frame(root,
                  width=500,
                  height=1000,
                  bg="#fff")
sideframe.place(x=450,y=80)

#add label
Label(logoframe,
      text="Exam Report",
      font=('Microsoft YaHei UI Light',20,'bold'),
      bg="#57a1f8",
      fg="White",
      width=45,
      anchor='center').place(x=0,y=20)

totscreentime = Label(sideframe,
                  text="Total Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=20)

authscreentime = Label(sideframe,
                  text="Total Authorized Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=80)

unauthscreentime = Label(sideframe,
                  text="Total Unuthorized Screen Time",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=140)

exid = Label(sideframe,
                  text="EXAM ID",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=220)

sid = Label(sideframe,
                  text="STUDENT ID",
                  font=('Microsoft YaHei UI Light',11),
                  bg="white",
                  fg='black').place(x=15,y=280)


#add entry box
totscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
totscreentime_entry.place(x=15,y=50)

authscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
authscreentime_entry.place(x=15,y=110)

unauthscreentime_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
unauthscreentime_entry.place(x=15,y=170)

exid_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
exid_entry.place(x=15,y=250)

sid_entry = Entry(sideframe,
                    width=25,
                    fg='Black',
                    border=1,
                    bg='White',
                    font=('Microsoft YaHei UI Light',11))
sid_entry.place(x=15,y=310)

#add button
exitbtn = Button(sideframe,
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
exitbtn.place(x=85,y=380)

startbtn = Button(sideframe,
                text="Load Data",
                bg="#57a1f8",
                fg="white",
                width=10,
                height=0,
                pady=2,
                cursor='hand2',
                border=0,
                font=('Microsoft YaHei UI Light',11, 'bold'),
                command=loaddata)
startbtn.place(x=70,y=350)

#add result table
my_tree = ttk.Treeview(root,height=18)
my_tree['columns'] = ("no","reason","date")
custom_font = ('Microsoft YaHei UI Light',10)
my_tree.tag_configure("custom_font",font=custom_font)
#set style
s = ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',bg='#57a1f8',font=('Microsoft YaHei UI Light',8, 'bold'), height=15)
s.configure('Treeview',rowheight=20)
#foramt column
my_tree.column('#0',width=0, stretch='no')
my_tree.column('no',width=50,anchor=CENTER)
my_tree.column('reason',width=200,anchor=W)
my_tree.column('date',width=180,anchor=W)
#create headding
my_tree.heading('no',text='No',anchor=CENTER)
my_tree.heading('reason',text='Reason',anchor=CENTER)
my_tree.heading('date',text='Date and Time',anchor=CENTER)

my_tree.place(x=10,y=100)

#showdata()

root.mainloop()