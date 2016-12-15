from tkinter import *

import smtplib

from tkinter import messagebox as tkMessageBox
def close_window():
    try:
        eid=e1.get()
        message=e3.get()

    
        to = eid
        gmail_user = 'vijaygarg680@gmail.com'
        gmail_pwd = 'inhuman((**^!%@!@'
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()

        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Vijay Garg Advocate \n'

        msg = header + message
        smtpserver.sendmail(gmail_user, to, msg)

        smtpserver.close()



        tkMessageBox.showinfo("CONGRATULATIONS!!!", "MESSAGE SENT SUCCESSFULLY!!")
    
        masterk.destroy()
        exec(open("mainpage1.py").read())
    except:
        
        tkMessageBox.showinfo("OHOO!!!", "SOME ERROR OCCURED.CHECK INTERNET CONNECTION")
        
        masterk.destroy()
        exec(open("mainpage1.py").read())

global back_image,masterk
masterk = Tk()
masterk.resizable(width=False, height=False)
masterk.geometry('900x695')
back_image=PhotoImage(file="brt.gif")
label=Label(masterk,image=back_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
global e1,e3


w1 = Label(masterk, text="Email id of client ",fg="black",bg='White',font=("Comic Sans MS", 14))
w1.grid(row=0,column=0,sticky=W,pady=(0,5))
e1 = Entry(masterk,font=("Comic Sans MS", 14))
e1.grid(row=0, column=1)



w3 = Label(masterk, text=" MESSAGE ",fg="black",bg='White',font=("Comic Sans MS", 14))
w3.grid(row=1,column=0,sticky=W,pady=(0,5))
e3 = Entry(masterk,font=("Comic Sans MS", 14))
e3.grid(row=1, column=1)

submitbutton=Button(masterk,text="Submit",command=close_window,fg="white",bg="green",font=("Helvetica", 16))
submitbutton.grid(row=2,column=1,columnspan=2,sticky=W)



