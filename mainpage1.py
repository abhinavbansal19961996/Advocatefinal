from tkinter import *
import sqlite3
import smtplib
import webbrowser
import random, pygame, sys
from pygame.locals import *
from tkinter import messagebox as tkMessageBox
import ctypes  # An included library with Python install.
from PyQt5.QtGui import QPalette,QBrush,QImage
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMessageBox
def newcase():
    master.destroy()
    exec(open("newcase.py").read())
def searchcase():
    master.destroy()
    exec(open("searchcase.py").read())
def game():
    try:
        exec(open("wormy.py").read())
    except:
        tkMessageBox.showinfo("Thanks", "Thanks for playing")
def deletecase():
    master.destroy()
    exec(open("delete.py").read())
def updatecase():
    master.destroy()
    exec(open("update.py").read())
def messagecase():
    master.destroy()
    exec(open("coolmessage.py").read())
def offweb():
    webbrowser.open_new(r"http://phhc.gov.in/")
def quote():
    import sqlite3


    convar = sqlite3.connect('count.db')


    query="SELECT i FROM counts;"

    cursor = convar.execute(query)
    for row in cursor:
        i=row[0]
    convar.commit()


    list=["Whenever I hear anyone arguing for slavery, I feel a strong impulse to see it tried on him personally.","Be sure you put your feet in the right place, then stand firm.","I have always found that mercy bears richer fruits than strict justice.","If you want to test a man’s character, give him power.","In the end, it’s not the years in your life that count. It’s the life in your years.","No man has a good enough memory to be a successful liar","Give me six hours to chop down a tree, and I will spend the first four sharpening the axe","God couldn’t be everywhere, so he created mothers.","Do one thing every day that scares you.","Dream big and dare to fail.","A jug fills drop by drop.","Learn from yesterday, live for today, hope for tomorrow.","The best revenge is massive success","Happiness will never come to those who fail to appreciate what they already have","Hope is a waking dream","We become what we think about","If you have never failed you have never lived.","Whatever you are, be a good one.","Don’t wait. The time will never be just right.","I hear and I forget, I see and I remember. I do and I understand.","It does not matter how slowly you go as long as you do not stop.","Don’t regret the past, just learn from it.","Santa: My dad was an extremely brave man. He once entered a lion's cage. Banta: He probably got a lot of applause ven he got out. Santa: I didn't say he got out.","Q: Why was Santa writing the exam near the door? A: Because it was an entrance exam.","Banta: Name the 3 fastest means of communication. Santa: Telephone, Television, Tell-a-woman","Santa & Banta got tired of mobile & decide 2 use pigeons. 1day a pigeon reaches Banta without message. Angry Banta calls Santa! Santa: Oye, this was a missed call","Frog: Tumhare paas dimaag nahin hai.Santa: Hai.Frog: Nahin hai.Santa: Hai.Frog: Nahin hai & jumps into the well.Santa: Isme suicide karne waali kya baat thi.?","Banta ek ! sadhu se bola Baba, meri biwi bahut pareshan karti hai, koi upay batao. Sadhu: Beta, upaay hota to main sadhu kyun banta?","Banta owned a factory. \n He issued orders that only married \n men would be employed. \nFriend asks: Why this ? \nBant reply: \nBecause married men are more obedient.","In an African Safari,A LION suddenly bounced on Santa's wife.WIFE-Shoot him! Shoot him!SANTA-Yes Yes.I'm changing d battery of my camera..","Santa: Look a thief has entered our kitchenand he is eating the cake I made.Banta: Whom should I call now,Police or Ambulance?","Banta: Marte waqt aadmi ko kya dena chahiye? Santa: Birla cement. Banta: Kyun? Santa: Kyunki is Cement mein jaan hai."]
    
    ctypes.windll.user32.MessageBoxW(0, list[i%32], "JOKES AND QUOTES", 0)
    i=i+1
    query="update counts set i=?"


    cursor = convar.execute(query,(i,))
    convar.commit()
    convar.close()

    

global master,back_image
master= Tk()
master.resizable(width=False, height=False)
master.geometry('900x695')
master.configure(background='DarkOrange4')
back_image=PhotoImage(file="law.gif")
label=Label(master,image=back_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
playButton = Button(master, text='New Case',fg="white",bg="brown",font=("Comic Sans MS", 16),command=newcase)
playButton.grid(row=0,column=0,padx=(0, 100),pady=(0,10))


playButton = Button(master, text='Update Case',fg="white",bg="brown",font=("Comic Sans MS", 16),command=updatecase)
playButton.grid(row=1,column=0,padx=(28, 100),pady=(0,10))


playButton = Button(master, text='Search Case',fg="white",bg="brown",font=("Comic Sans MS", 16),command=searchcase)
playButton.grid(row=2,column=0,padx=(28, 100),pady=(0,10))


playButton = Button(master, text='Delete Case',fg="white",bg="brown",font=("Comic Sans MS", 16),command=deletecase)
playButton.grid(row=3,column=0,padx=(28, 100),pady=(0,10))


playButton = Button(master, text='Send Email',fg="white",bg="brown",font=("Comic Sans MS", 16),command=messagecase)
playButton.grid(row=0,column=1,padx=(0, 0))


playButton = Button(master, text='Official Website',fg="white",bg="brown",font=("Comic Sans MS", 16),command=offweb)
playButton.grid(row=1,column=1,padx=(60,0 ))


playButton = Button(master, text='Jokes & Quotes',fg="white",bg="brown",font=("Comic Sans MS", 16),command=quote)
playButton.grid(row=2,column=1,padx=(45, 0))


playButton = Button(master, text='Leisure Game',fg="white",bg="brown",font=("Comic Sans MS", 16),command=game)
playButton.grid(row=3,column=1,padx=(23,0))
master.mainloop()
