from tkinter import *
import tkinter as tk 
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def update_gif(frame):
    # Update the GIF frame
    frame_index = (frame + 1) % len(frames)
    img = frames[frame_index]
    label.config(image=img)
    label.image = img
    root.after(50, update_gif, frame_index)
    
def exitbtncommand():
    #message box
    result = messagebox.askyesno("Confirmation","Do you want to exit?")
    #system exit code
    if result:
        root.destroy()
        
def loginasadmin():
    root.destroy()
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/adminLogin.py'], check=True)

def loginasstudent():
    root.destroy()
    result = subprocess.run(['python', 'C:/Users/DELL/Desktop/Python/Project parts/final Project/studentlogin.py'], check=True)

#create window
root = tk.Tk()
#window title
root.title("LearnMaster Education Application 2.0")
#background colour of window
root.configure(background="white")
#set screen height and weight
root.geometry("925x500+300+200")
# Disable maximize option
root.resizable(False, False)

# Open the GIF file with Pillow
gif_path = "C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/world.gif"
gif = Image.open(gif_path)

# Extract individual frames from the animated GIF
frames = []
try:
    for i in range(gif.n_frames):
        gif.seek(i)
        frame = ImageTk.PhotoImage(gif.copy())
        frames.append(frame)
except EOFError:
    pass

# Display the first frame initially
label = tk.Label(root,
                image=frames[0],
                bg="white")
label.place(x=50,y=0)

# Schedule the update function to create animation
root.after(0, update_gif, 0)

studentlog = tk.Button(root,
       width=25,
       pady=7,
       text='Sign in as Student',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       font=('Microsoft YaHei UI Light',13,'bold'),
       command=loginasstudent)
studentlog.place(x=550,y=244)

adminlog = tk.Button(root,
       width=25,
       pady=7,
       text='Sign in as Admin',
       bg="#57a1f8",
       fg='white',
       border=0,
       cursor='hand2',
       font=('Microsoft YaHei UI Light',13,'bold'),
       command=loginasadmin)
adminlog.place(x=550,y=304)

exit = tk.Label(root,
                 text="Do you need to exit?",
                 fg='black',
                 bg='white',
                 width=39,
                 cursor="hand2",
                 font=('Microsoft YaHei UI Light',8,'bold'),
                 anchor="center")
exit.place(x=550,y=364)
exit.bind("<Button-1>",lambda event: exitbtncommand())

img = PhotoImage(file='C:/Users/DELL/Desktop/Python/Project parts/final Project/Images/logosmall.gif')

Label(root,
      image=img,
      bg='White').place(x=570,y=50)

root.mainloop()