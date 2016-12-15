from tkinter import *
import sqlite3


from tkinter import messagebox as tkMessageBox


def closed_window():
    
    koot.destroy()
    exec(open("mainpage1.py").read())
   
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=870,height=550)


def decisions(se):
    
    global option,fileno_window,casenos_window,filenos_window,noc_window,pname_window,type_window,status_window,feepaid_window
    global optionq,e1,var,var1,closed_window
    sea=str(se)
    if sea=="File no":

        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=filenos_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=filenos_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
    if sea=="Case no" :
        
        
        
        case_type=["CWP","CRM-M","","CR","RSA","CRR","CRA-S","FAO","CM","CRM","ARB","CA","CACP","CAPP","CCEC","CCES","CEA","CEC","CEGC","CESR","CLAIM","CMA","CMM","CO","COA","COCP","CP","CRA","CRA-AD","CRA-AS","CRA-D","CRACP","CREF","CRM-A","CRM-W","CROCP","CRR(F)","CRREF","CRWP","CS","CS-OS","CUSAP","DP","EA","EDC","EDREF","EFA","EP","ESA","FAO(FC)","FAO-C","FAO-M","GCR","GSTR","GTA","GTC","GTR","GVATR","INCOMP","INTTA","IOIN","ITA","ITC","ITR","LPA","LR","MATRF","MRC","O&M","OLR","PBT","PVR","RA","RA-CA","RA-CP","RA-CR","RA-CW","RA-LP","RA-RF","RA-RS","RCRWP","RFA","RP","SA","SAO","SDR","STA","STC","STR","TA","TC","TCRM","UVA","UVR","VATAP","VATCASE","VATREF","WTA","WTC","WTR","XOBJ","XOBJC","XOBJL","XOBJR","XOBJS","OTHER"]
        var = StringVar()           #dec. a String var
        var.set("")  # set initial initial value
        option = OptionMenu(root, var, *case_type)
        option.grid(row=1,column=2,sticky=W,padx=55)


        e1 = Entry(root,font=("Comic Sans MS", 14))
        e1.grid(row=1, column=1)

        

        case_year=["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
        var1 = StringVar()           #dec. a String var
        var1.set("")  # set initial initial value
        optionq = OptionMenu(root, var1, *case_year)
        optionq.grid(row=1,column=3,sticky=W,columnspan=2,padx=(10,0))
        
        
        loginbutton=Button(root,text="SEARCH",command=casenos_window,fg="white",bg="green",font=("Helvetica", 14))
        loginbutton.grid(row=2,column=2)
        submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
        submitbutton.grid(row=2,column=3)

    if sea=="Fee paid":
        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=feepaid_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=feepaid_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
    if sea=="Status":
        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=status_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=status_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
    if sea=="Type":
        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=type_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=type_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
    if sea=="Parties name":
        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=pname_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=pname_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
    if sea=="Name of opposite counsel":
        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=noc_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            
            loginbutton=Button(root,text="SEARCH",command=noc_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
    if sea=="All":

        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=fileno_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(root,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(root,text="SEARCH",command=fileno_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            submitbutton=Button(root,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)


def noc_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where noc LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()



def pname_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where pn LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()

def type_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where type LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()




def status_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where status LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()

    

def feepaid_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where fp LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()

    
def casenos_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    pqw=var.get()
    pwq=var1.get()
    qwer=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where cwp LIKE ? and nmbr LIKE ? and year LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+pqw+'%','%'+qwer+'%','%'+pwq+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()


def filenos_window():
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where fn LIKE ?"
    i=0
    cursor = convar.execute(query,('%'+s+'%',))
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()

def fileno_window():
    
    global frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails;"
    i=0
    cursor = convar.execute(query)
    w3 = Label(frame, text="File no",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=0)
    w3 = Label(frame, text="Case Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=1)
    w3 = Label(frame, text="Case No.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=2)
    w3 = Label(frame, text="Year",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=3)
    w3 = Label(frame, text="Parties name",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=4)
    w3 = Label(frame, text="Name of opposite counsel",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=5)
    w3 = Label(frame, text="Date Fixed",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=6)
    w3 = Label(frame, text="Date Pending",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=7)
    w3 = Label(frame, text="Status",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=8)
    w3 = Label(frame, text="Type",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=9)
    w3 = Label(frame, text="Fee Paid",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=10)
    w3 = Label(frame, text="Additional fee details",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=11)
    w3 = Label(frame, text="Email",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=12)
    w3 = Label(frame, text="Phone no.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=13)
    w3 = Label(frame, text="Other Details.",fg="black",font=("Helvetica" ,12,"bold"))
    w3.grid(row=i,column=14)

    i=i+1
 

    
        

    for row in cursor:
        w3 = Label(frame, text=row[0],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=0)
        w3 = Label(frame, text=row[1],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=1)
        w3 = Label(frame, text=row[2],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=2)
        w3 = Label(frame, text=row[3],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=3)
        w3 = Label(frame, text=row[4],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=4)
        w3 = Label(frame, text=row[5],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=5)
        w3 = Label(frame, text=row[6],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=6)
        w3 = Label(frame, text=row[7],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=7)
        w3 = Label(frame, text=row[8],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=8)
        w3 = Label(frame, text=row[9],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=9)
        w3 = Label(frame, text=row[10],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=10)
        w3 = Label(frame, text=row[11],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=11)
        w3 = Label(frame, text=row[12],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=12)
        w3 = Label(frame, text=row[13],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=13)
        w3 = Label(frame, text=row[14],fg="black",font=("Helvetica" ,12,"bold"))
        w3.grid(row=i,column=14)
        i=i+1

    convar.commit()
     

    convar.close()




    
global root,koot
global i,var2,label,optione
i=1
koot = Tk()
koot.resizable(width=False, height=False)
koot.geometry('900x695')
koot.configure(background='SystemButtonFace')

root = Frame(koot,width=900,height=80)
root.grid_propagate(0)
root.grid(row=0, column=0,sticky=N)
global back_images
back_images=PhotoImage(file="brt.gif")
label=Label(root,image=back_images)
label.place(x=0, y=0, relwidth=1, relheight=1)





decision=["File no","Case no","Fee paid","Status","Type","Parties name","Name of opposite counsel","All"]
var2 = StringVar()           #dec. a String var
var2.set("Search by")  # set initial initial value
optione = OptionMenu(root, var2, *decision,command=decisions)
optione.grid(row=1,column=0,sticky=W,padx=(80,0))


## 2nd frame
roots = Frame(koot,width=900,height=615,bg='SystemButtonFace')
roots.grid_propagate(0)

roots.grid(row=1, column=0)

global canvas
canvas=Canvas(roots)
frame=Frame(canvas,width=900,height=615,bg='SystemButtonFace')


myscrollbar=Scrollbar(roots,orient="horizontal",command=canvas.xview)
canvas.configure(xscrollcommand=myscrollbar.set)

myscrollbar.pack(side="bottom",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)


