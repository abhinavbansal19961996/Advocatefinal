##FIXING WINDOW SIZE ...
from tkinter import *
from tkinter import messagebox as tkMessageBox
import sqlite3
import webbrowser
import ctypes
import random, pygame, sys
from pygame.locals import *

import smtplib


def close_window(): 
    
    name=e1.get()
    password=e2.get()
    if name=="vijay":
        if password=="vijay":
            masterss.destroy()
            exec(open("mainpage1.py").read())
        else:
            tkMessageBox.showinfo("Login Error", "Incorrect password!")
    else:
        if password=="vijay":
            tkMessageBox.showinfo("Login Error", "Incorrect username!")
        else:
            tkMessageBox.showinfo("Login Error", "Incorrect username and password!")

global masterss
masterss = Tk()
masterss.resizable(width=False, height=False)
masterss.geometry('900x695')
masterss.configure(background='DarkOrange4')
root = Frame(masterss,width=350,height=695)
root.grid_propagate(0)
root.grid(row=0, column=0)
myImage = PhotoImage(file='casi.gif')
k=myImage.subsample(1,1)
k=k.zoom(1,1)
w = Label(root, image=k)
#w.place(x=0,y=0)
w.grid(row=0, column=0)



##bg='SystemButtonFace'
roots =Frame(masterss,width=560,height=695,bg='saddle brown')
roots.grid_propagate(0)

roots.grid(row=0, column=1)
myImagess = PhotoImage(file='vijay.gif')
w = Label(roots, image=myImagess)
w.grid(row=2,column=2,rowspan=2,padx=20)
w3 = Label(roots, text=" Er. Abhinav Bansal ",bg='saddle brown',fg="black",font=("Helvetica" ,12,"bold"))
w4 = Label(roots, text="Version 1.0... ",fg="black",bg='saddle brown',font=("Helvetica", 8))
w1 = Label(roots, text="USERNAME ",fg="black",bg='saddle brown',font=("Comic Sans MS", 14))
e1 = Entry(roots,font=("Comic Sans MS", 14))
w2 = Label(roots, text="PASSWORD",fg="black",bg='saddle brown',font=("Comic Sans MS", 14))
e2 = Entry(roots,font=("Comic Sans MS", 14))
loginbutton=Button(roots,text="SIGN IN",command=close_window,fg="white",bg="green",font=("Helvetica", 16))
loginbutton.grid(row=5,column=1)
w3.grid(row=0,column=0)
w4.grid(row=1,column=0)
w1.grid(row=2,column=0)
w2.grid(row=3,column=0)



e1.grid(row=2, column=1)
e2.grid(row=3, column=1)



root.mainloop()
