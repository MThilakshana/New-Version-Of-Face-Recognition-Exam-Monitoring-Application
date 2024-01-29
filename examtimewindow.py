from tkinter import *
import mysql.connector
import cv2
from tkinter import messagebox
from datetime import datetime
import face_recognition
import time

examimagepath = ""
    
#compair images
def compairImages():
    
    #find face function
    def find_face(img_path):
        image = cv2.imread(img_path)
        face_enc = face_recognition.face_encodings(image)
        
        if not face_enc:
            print("No face")
            return None
        
        return face_enc[0]
    
    imageCount = 1
    
    sql = "SELECT COUNT(*) FROM classdatainstudentview"
    cursor.execute(sql)
    number_of_images = cursor.fetchone()[0]
    
    firstpath = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/"
    firstimagename = "{}MyImage{}.png".format(firstpath,str(imageCount))
    
    secondpath = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/ExamTime/"
    secondimagename = "{}MyImage{}.png".format(secondpath,"1")
    
    image1 = find_face(firstimagename)
    image2 = find_face(secondimagename)
    
    is_same = face_recognition.compare_faces([image1], image2)[0]
    print(f"Is same : {is_same}")
    
    if is_same:
        distance = face_recognition.face_distance([image1],image2)
        distance = round(distance[0]*100)
        accuracy = 100 - round(distance)
        print("The images are the same")
        print(f"Accuracy level: {accuracy}%")
    else:
        print("the images are not same")

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
    
    messagebox.showinfo("Important","Press space to enter class\nWhen open the camera otherwise\npress ecs to exit")
    
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Image Capture")
    
    while True:
        ret, frame = cam.read()
        if not ret:
            messagebox.showinfo("Warning","Image Capture Error")
            break
        
        cv2.imshow("LearnMaster - 1.0",frame)
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
        
    cam.release()
    cv2.destroyAllWindows()
        
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

