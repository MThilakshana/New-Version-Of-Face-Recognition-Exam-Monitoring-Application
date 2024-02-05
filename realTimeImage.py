from tkinter import *
import cv2
import face_recognition
import os
import time

sidVal = ""
eidVal = ""


def get_data(exam_id, student_id):
    print(f"Student ID: {student_id}")
    print(f"Exam ID: {exam_id}")

# Load known faces from the specified folder
def load_known_faces(folder_path):
    known_faces = []

    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)

    return known_faces

# Identify the candidate in the current frame
def identify_candidate(frame, known_faces):
    rgb_frame = frame[:, :, ::-1]  # Convert to RGB for face_recognition
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        if True in matches:
            return "authorized"
    return "unauthorized"

# Capture and process frames
def capture_and_process_frames(known_faces):
    video_capture = cv2.VideoCapture(0)

    total_authorized_time = 0
    total_unauthorized_time = 0
    unauthorized_start_time = None
    total_screen_time = 0
    last_seen = None
    unauthorized_printed = False

    while True:
        ret, frame = video_capture.read()

        person_type = identify_candidate(frame, known_faces)

        if person_type == "authorized":
            if last_seen is None:
                start_time = time.time()
                last_seen = start_time
            else:
                total_authorized_time += time.time() - last_seen
                last_seen = time.time()
            color = (0, 255, 0)  # Green color for authorized
            # Reset unauthorized timer and flag
            unauthorized_start_time = None
            unauthorized_printed = False
        else:
            if last_seen is not None:
                total_unauthorized_time += time.time() - last_seen
                last_seen = time.time()
                # Check if unauthorized time exceeds 8 seconds continuously
                if unauthorized_start_time is None:
                    unauthorized_start_time = time.time()
                elif time.time() - unauthorized_start_time > 8 and not unauthorized_printed:
                    print(f"Authorized person not detected at {time.strftime('%Y-%m-%d %H:%M:%S')}!")
                    unauthorized_printed = True
            else:
                # Set unauthorized start time when a person is first detected
                unauthorized_start_time = time.time()
                unauthorized_printed = False
            color = (0, 0, 255)  # Red color for unauthorized

        # Display the frame with colored text
        cv2.putText(frame, f"Person Type: {person_type}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        cv2.imshow('Video', frame)

        # Update total screen time
        total_screen_time = time.time() - start_time if last_seen else 0

        # Break the loop if 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # 27 is the ASCII code for 'Esc'
            break

    video_capture.release()
    cv2.destroyAllWindows()

    # Print the total screen time for authorized and unauthorized persons
    print(f"Total Authorized Screen Time: {total_authorized_time} seconds")
    print(f"Total Unauthorized Screen Time: {total_unauthorized_time} seconds")
    print(f"Total Screen Time Camera Turned On: {total_screen_time} seconds")

    #convert string to float
    float_authorized_time = float(total_authorized_time)
    float_unauthorized_time = float(total_unauthorized_time)
    float_screen_time = float(total_screen_time)
    
    #make values as rounded
    float_authorized_time = round(float_authorized_time , 2)
    float_unauthorized_time = round(float_unauthorized_time, 2)
    float_screen_time = round(float_screen_time, 2)
    
    #build last window
    root=Tk()
    root.title('End Exam Report - LearnMaster 1.0')
    root.geometry('310x300+300+200')
    root.configure(bg="#fff")
    root.resizable(False,False)

    frame_win = Frame(root,
                width=300,
                height=300,
                bg='white')
    frame_win.place(x=10,y=0)

    #add heading
    heading = Label(frame_win,
                    text='End Exam Report',
                    fg='#57a1f8',
                    bg='white',
                    font=('Microsoft YaHei UI Light',17,'bold'))
    heading.place(x=40,y=0)
    
    Label(frame_win,
      text="Student ID",
      font=('Microsoft YaHei UI Light',11,),
      bg='white',
      fg='black').place(x=0,y=50)

    Label(frame_win,
        text="Exam ID",
        bg='white',
        font=('Microsoft YaHei UI Light',11,),
        fg='black').place(x=0,y=100)

    Label(frame_win,
        text="Authorized Time",
        bg='white',
        font=('Microsoft YaHei UI Light',11,),
        fg='black').place(x=0,y=150)
    
    Label(frame_win,
        text="Full Screen Time",
        bg='white',
        font=('Microsoft YaHei UI Light',11,),
        fg='black').place(x=0,y=200)
    
    stuEntry = Entry(frame_win,
                    font=('Microsoft YaHei UI Light',11,),
                    bg='white',
                    fg='black')
    stuEntry.place(x=125,y=50)

    exmEntry = Entry(frame_win,
                    font=('Microsoft YaHei UI Light',11,),
                    bg='white',
                    fg='black')
    exmEntry.place(x=125,y=100)

    autEntry = Entry(frame_win,
                    font=('Microsoft YaHei UI Light',11,),
                    bg='white',
                    fg='black')
    autEntry.place(x=125,y=150)

    sctEntry = Entry(frame_win,
                    font=('Microsoft YaHei UI Light',11,),
                    bg='white',
                    fg='black')
    sctEntry.place(x=125,y=200)

    Button(frame_win,
        width=30,
        pady=7,
        text='End Exam',
        bg="#57a1f8",
        fg='white',
        border=0,
        cursor='hand2',
        command=root.destroy).place(x=45,y=250)
    
    autEntry.insert(0,str(float_authorized_time) + " Sec")
    sctEntry.insert(0,str(float_screen_time) + " Sec")

    root.mainloop()
    
# Specify the folder path where candidate images are stored
candidates_folder = "C:/Users/DELL/Desktop/Python/Project parts/final Project/CapturedImage/ExamTime"

# Load the known faces
known_faces = load_known_faces(candidates_folder)

# Start capturing and processing frames
capture_and_process_frames(known_faces)
