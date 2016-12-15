from tkinter import *
import sqlite3

from tkinter import messagebox as tkMessageBox
def closes_window():
    masters.destroy()
    exec(open("mainpage1.py").read())
    
def close_window():
    a1=e1.get()
    a2=var.get()
    a3=e2.get()
    a4=var1.get()
    a5=e3.get()
    a6=e4.get()
    a7=e5.get()
    a8=e6.get()
    a9=e7.get()
    a10=e8.get()
    a11=var2.get()
    a12=e10.get()
    a13=e11.get()
    a14=e12.get()
    a15=e13.get()
    
    convar = sqlite3.connect('case.db')
    query='''INSERT INTO casedetails (fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');'''%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15)
    convar.execute(query)
    convar.commit()
    convar.close()




    
    tkMessageBox.showinfo("CONGRATULATIONS", "DATA SUBMITTED SUCCESSFULLY!!")
    masters.destroy()
    exec(open("mainpage1.py").read())
    
global masters
masters = Tk()
masters.resizable(width=False, height=False)
masters.geometry('900x695')
back_image=PhotoImage(file="brt.gif")
label=Label(masters,image=back_image)
label.place(x=0, y=0, relwidth=1, relheight=1)
global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,var,var1,var2


w1 = Label(masters, text="FILE NO ",fg="black",bg='White',font=("Comic Sans MS", 14))
w1.grid(row=0,column=0,sticky=W,pady=(0,5))
e1 = Entry(masters,font=("Comic Sans MS", 14))
e1.grid(row=0, column=1)

w2 = Label(masters, text="CASE NO ",fg="black",font=("Comic Sans MS", 14))
w2.grid(row=1,column=0,sticky=W,pady=(0,5))


case_type=["CWP","CRM-M","CR","RSA","CRR","CRA-S","FAO","CM","CRM","ARB","CA","CACP","CAPP","CCEC","CCES","CEA","CEC","CEGC","CESR","CLAIM","CMA","CMM","CO","COA","COCP","CP","CRA","CRA-AD","CRA-AS","CRA-D","CRACP","CREF","CRM-A","CRM-W","CROCP","CRR(F)","CRREF","CRWP","CS","CS-OS","CUSAP","DP","EA","EDC","EDREF","EFA","EP","ESA","FAO(FC)","FAO-C","FAO-M","GCR","GSTR","GTA","GTC","GTR","GVATR","INCOMP","INTTA","IOIN","ITA","ITC","ITR","LPA","LR","MATRF","MRC","O&M","OLR","PBT","PVR","RA","RA-CA","RA-CP","RA-CR","RA-CW","RA-LP","RA-RF","RA-RS","RCRWP","RFA","RP","SA","SAO","SDR","STA","STC","STR","TA","TC","TCRM","UVA","UVR","VATAP","VATCASE","VATREF","WTA","WTC","WTR","XOBJ","XOBJC","XOBJL","XOBJR","XOBJS","OTHER"]
var = StringVar()           #dec. a String var
var.set("Case Type")  # set initial initial value
option = OptionMenu(masters, var, *case_type)
option.grid(row=1,column=1,sticky=W,padx=55)


e2 = Entry(masters,font=("Comic Sans MS", 14))
e2.grid(row=1, column=1,sticky=E,padx=160,columnspan=2)


case_year=["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
var1 = StringVar()           #dec. a String var
var1.set("Case Year")  # set initial initial value
optionq = OptionMenu(masters, var1, *case_year)
optionq.grid(row=1,column=2,sticky=W,columnspan=2,padx=(10,0))



w3 = Label(masters, text=" PARTIES NAME ",fg="black",bg='White',font=("Comic Sans MS", 14))
w3.grid(row=2,column=0,sticky=W,pady=(0,5))
e3 = Entry(masters,font=("Comic Sans MS", 14))
e3.grid(row=2, column=1)


w4 = Label(masters, text="NAME OF OPPOSITE COUNSEL",fg="black",font=("Comic Sans MS", 14))
w4.grid(row=3,column=0,sticky=W,padx=(0,10),pady=(0,5))
e4 = Entry(masters,font=("Comic Sans MS", 14))
e4.grid(row=3, column=1)


w5 = Label(masters, text="DATE FIXED",fg="black",bg='White',font=("Comic Sans MS", 14))
w5.grid(row=4,column=0,sticky=W,pady=(0,5))
e5 = Entry(masters,font=("Comic Sans MS", 14))
e5.grid(row=4, column=1)


w6 = Label(masters, text="DATE PENDING",fg="black",font=("Comic Sans MS", 14))
w6.grid(row=5,column=0,sticky=W,pady=(0,5))
e6 = Entry(masters,font=("Comic Sans MS", 14))
e6.grid(row=5, column=1)

w7 = Label(masters, text="STATUS",fg="black",bg='White',font=("Comic Sans MS", 14))
w7.grid(row=6,column=0,sticky=W,pady=(0,5))
e7 = Entry(masters,font=("Comic Sans MS", 14))
e7.grid(row=6, column=1)

w8 = Label(masters, text="TYPE",fg="black",font=("Comic Sans MS", 14))
w8.grid(row=7,column=0,sticky=W,pady=(0,5))
e8 = Entry(masters,font=("Comic Sans MS", 14))
e8.grid(row=7, column=1)


w9 = Label(masters, text="FEE PAID",fg="black",bg='White',font=("Comic Sans MS", 14))
w9.grid(row=8,column=0,sticky=W,pady=(0,5))
decision=["YES","NO","NONE"]
var2 = StringVar()           #dec. a String var
var2.set("Fee Paid?")  # set initial initial value
optione = OptionMenu(masters, var2, *decision)
optione.grid(row=8,column=1,sticky=W,padx=(80,0))



w10 = Label(masters, text="ADDITIONAL FEE DETAILS ",fg="black",font=("Comic Sans MS", 14))
w10.grid(row=9,column=0,sticky=W,pady=(0,5))
e10 = Entry(masters,font=("Comic Sans MS", 14))
e10.grid(row=9, column=1)


w11 = Label(masters, text="EMAIL ",fg="black",bg='White',font=("Comic Sans MS", 14))
w11.grid(row=10,column=0,sticky=W,pady=(0,5))
e11 = Entry(masters,font=("Comic Sans MS", 14))
e11.grid(row=10,column=1)


w12 = Label(masters, text="PHONE NO ",fg="black",font=("Comic Sans MS", 14))
w12.grid(row=11,column=0,sticky=W,pady=(0,5))
e12 = Entry(masters,font=("Comic Sans MS", 14))
e12.grid(row=11, column=1)


w13 = Label(masters, text="OTHER DETAILS",fg="black",bg='White',font=("Comic Sans MS", 14))
w13.grid(row=12,column=0,sticky=W,pady=(0,5))
e13 = Entry(masters,font=("Comic Sans MS", 14))
e13.grid(row=12, column=1)


w13 = Label(masters,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
w13.grid(row=13,column=0,columnspan=3,sticky=W,pady=(0,0))


submitbutton=Button(masters,text="Submit",command=close_window,fg="white",bg="green",font=("Helvetica", 16))
submitbutton.grid(row=14,column=1,columnspan=2,sticky=W)

submitbutton=Button(masters,text="Close",command=closes_window,fg="white",bg="green",font=("Helvetica", 16))
submitbutton.grid(row=14,column=1,padx=30,sticky=E)


w13 = Label(masters,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
w13.grid(row=15,column=0,columnspan=3,sticky=W,pady=(0,0))


masters.mainloop()
