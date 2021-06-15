from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import admin_login
import student_login
import student_management

 
root=Tk()
root.title("SDM")
root.geometry('1350x750+0+0')
root.config(bg="powder blue")
root.resizable(0,0)


l1=Label(root,text="STUDENT DATABASE MANAGEMENT SYSTEM",font=('arial',40,'bold'))
l1.pack()
b1=Button(root,text="STUDENT LOGIN",bg="MistyRose2",fg="Black",width=17,height=3,font=('arial',30,'bold'))
b1.place(x=470,y=150)
b1.config(command=student_login.main)

b1=Button(root,text="ADMINISTER LOGIN",bg="MistyRose2",fg="Black",width=17,height=3,font=('arial',30,'bold'))
b1.place(x=470,y=400)
b1.config(command=admin_login.main)
'''b1.config(command=student_management.main)'''

