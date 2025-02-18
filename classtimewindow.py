from tkinter import *
import mysql.connector
import cv2
from tkinter import messagebox
from datetime import datetime
import pyrebase

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

#function for capture images from web cam
def captureImage(database):
    stu_data = database.child("ClassDataInStudentView").get()
    stu_data_val = stu_data.val()
    imagecount = len(stu_data_val)
    imagepath = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/ExamTime/"
    
    messagebox.showinfo("Important","Press space to enter class\nWhen open the camera otherwise\npress ecs to exit")
    
    #capture image
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Image Capture")
    
    while True:
        ret, frame = cam.read()
        if not ret:
            messagebox.showinfo("Warning","Image capturing Error!")
            break
        
        cv2.imshow("LearnMaster - 2.0",frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            print("closing...")
            break
        if k%256 == 32:
            img_name = "{}MyImage{}.png".format(imagepath,imagecount)
            cv2.imwrite(img_name,frame)
            print("Image Captured")
            print("closing...")
            break
        
        '''imagename = "{}MyImage{}.png".format(imagepath,str(imagecount))
        cv2.imshow("LearnMaster - 1.0",frame)
        cv2.imwrite(imagename,frame)'''
        
    cam.release()
    cv2.destroyAllWindows()

def endclassbutton(class_id,student_id,root,database):
    cls_id = class_id
    stu_id = student_id
    
    #get current date
    current_datetime = datetime.now()
    current_date_string = current_datetime.strftime('%Y-%m-%d')
    
    #get current time
    current_time = datetime.now().time()
    current_time_string = current_time.strftime('%H:%M:%S')

    data_to_save = {"classid":class_id,"studentid":stu_id,"date":current_date_string,"time":current_time_string}
    path = str(class_id)+"_"+str(stu_id)
    database.child("ClassDataInStudentView").child(path).set(data_to_save)
    messagebox.showinfo("Message","Data Saved!")
    root.destroy()
    
def assignvalue(cid,sid):
    class_id = cid
    student_id = sid
    
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
    
    captureImage(database)
    
    root=Tk()
    root.title('End Class - LearnMaster 2.0')
    root.geometry('300x180+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    cidText = "Class ID - "+class_id
    sidText = "Student ID - "+student_id
    
    Label(root,
        text=cidText,
        font=('Microsoft YaHei UI Light',12, 'bold'),
        bg="white",
        fg='black').pack(fill=X,pady=20)
    
    Label(root,
        text=sidText,
        font=('Microsoft YaHei UI Light',12, 'bold'),
        bg="white",
        fg='black').pack(fill=X)
    
    #add button
    endbtn = Button(root,
                    width=30,
                    pady=7,
                    text='End Class',
                    bg="#57a1f8",
                    fg='white',
                    border=0,
                    cursor='hand2',
                    command=lambda: endclassbutton(class_id,student_id,root,database))
    endbtn.pack(fill=X,pady=20,padx=40)

    root.mainloop()

