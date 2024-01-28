from tkinter import *
import mysql.connector
import cv2
from tkinter import messagebox
from datetime import datetime
import face_recognition
import time

examimagepath = ""

#find face function
def find_face(img_path):
    image = cv2.imread(img_path)
    print("point 4 ########################################")
    face_enc = face_recognition.face_encodings(image)
    print("point 5 ########################################")
    return face_enc[0]
    
#compair images
def compairImages():
    imageCount = 1
    
    sql = "SELECT COUNT(*) FROM classdatainstudentview"
    cursor.execute(sql)
    number_of_images = cursor.fetchone()[0]
    print("point 1 ########################################")
    
    while(imageCount<=number_of_images):
        firstpath = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/"
        firstimagename = "{}MyImage{}.png".format(firstpath,str(imageCount))
        print("point 2 ########################################")
        secondimagename = examimagepath
        
        image1 = find_face(firstimagename)
        print("point 8 ########################################")
        image2 = find_face(secondimagename)
        print("point 3 ########################################")
        if image1 is not None and image2 is not None:
            is_same = face_recognition.compare_faces([image1], image2)[0]
            print("point 6 ########################################")
            print(f"Is same : {is_same}")
        else:
            print("error found")
        
        imageCount += 1

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

#function for capture images from web cam
def captureImage():
    sql = "SELECT COUNT(*) FROM examdatainstudentview"
    cursor.execute(sql)
    imagecount = int(cursor.fetchone()[0]) + 1
    imagepath = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/ExamTime/"
    #capture image
    cam = cv2.VideoCapture(0)
    
    while True:
        ret, frame= cam.read()
        if not ret:
            messagebox.showinfo("Warning","Image capturing Error!")
        else:
            imagename = "{}MyImage{}.png".format(imagepath,str(imagecount))
            cv2.imwrite(imagename,frame)
            time.sleep(5)
            cam.release()
            cv2.destroyAllWindows()
            examimagepath = imagename
        
def endexambutton(exam_id,student_id,root):
    exm_id = exam_id
    stu_id = student_id
    
    #get current date
    current_datetime = datetime.now()
    current_date_string = current_datetime.strftime('%Y-%m-%d')
    
    #get current time
    current_time = datetime.now().time()
    current_time_string = current_time.strftime('%H:%M:%S')
    
    record = (exm_id,stu_id,current_date_string,current_time_string)
    sql = "INSERT INTO examdatainstudentview VALUES(%s,%s,%s,%s)"

    cursor.execute(sql,record)
    mydb.commit()
    cursor.close()
    messagebox.showinfo("Message","Data Saved!")
    root.destroy()
    
def assignvalue(eid,sid):
    exam_id = eid
    student_id = sid
    
    captureImage()
    
    root=Tk()
    root.title('End Exam - LearnMaster 1.0')
    root.geometry('300x180+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    eidText = "Exam ID - "+exam_id
    sidText = "Student ID - "+student_id
    
    Label(root,
        text=eidText,
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
                    text='End Exam',
                    bg="#57a1f8",
                    fg='white',
                    border=0,
                    cursor='hand2',
                    command=lambda: endexambutton(exam_id,student_id,root))
    endbtn.pack(fill=X,pady=20,padx=40)
    
    compairImages()

    root.mainloop()

