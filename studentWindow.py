from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import subprocess

#connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="learnmaster"
)
cursor = mydb.cursor()

root=Tk()
root.title('Student Dashboard - LearnMaster 1.0')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

root.mainloop()