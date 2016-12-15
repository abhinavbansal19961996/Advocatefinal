from tkinter import *
import sqlite3

from tkinter import messagebox as tkMessageBox
def closed_window():
    
    masteru.destroy()
    exec(open("mainpage1.py").read())



from tkinter import messagebox as tkMessageBox
def decisions(se):
    
    global option,fileno_window,casenos_window,filenos_window,noc_window,pname_window,type_window,status_window,feepaid_window
    global optionq,e1,var,var1,closed_window
    sea=str(se)
    if sea=="File no":

        try:
            option.grid_forget()
            optionq.grid_forget()

            e1 = Entry(masteru,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(masteru,text="DELETE",command=filenos_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            
            submitbutton=Button(masteru,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
        except:
            e1 = Entry(masteru,font=("Comic Sans MS", 14))
            e1.grid(row=1, column=1)
            loginbutton=Button(masteru,text="DELETE",command=filenos_window,fg="white",bg="green",font=("Helvetica", 14))
            loginbutton.grid(row=2,column=2)
            
            submitbutton=Button(masteru,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
            submitbutton.grid(row=2,column=3)
            
    if sea=="Case no" :
        
        
        
        case_type=["CWP","CRM-M","","CR","RSA","CRR","CRA-S","FAO","CM","CRM","ARB","CA","CACP","CAPP","CCEC","CCES","CEA","CEC","CEGC","CESR","CLAIM","CMA","CMM","CO","COA","COCP","CP","CRA","CRA-AD","CRA-AS","CRA-D","CRACP","CREF","CRM-A","CRM-W","CROCP","CRR(F)","CRREF","CRWP","CS","CS-OS","CUSAP","DP","EA","EDC","EDREF","EFA","EP","ESA","FAO(FC)","FAO-C","FAO-M","GCR","GSTR","GTA","GTC","GTR","GVATR","INCOMP","INTTA","IOIN","ITA","ITC","ITR","LPA","LR","MATRF","MRC","O&M","OLR","PBT","PVR","RA","RA-CA","RA-CP","RA-CR","RA-CW","RA-LP","RA-RF","RA-RS","RCRWP","RFA","RP","SA","SAO","SDR","STA","STC","STR","TA","TC","TCRM","UVA","UVR","VATAP","VATCASE","VATREF","WTA","WTC","WTR","XOBJ","XOBJC","XOBJL","XOBJR","XOBJS","OTHER"]
        var = StringVar()           #dec. a String var
        var.set("")  # set initial initial value
        option = OptionMenu(masteru, var, *case_type)
        option.grid(row=1,column=2,sticky=W,padx=55)


        e1 = Entry(masteru,font=("Comic Sans MS", 14))
        e1.grid(row=1, column=1)

        

        case_year=["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
        var1 = StringVar()           #dec. a String var
        var1.set("")  # set initial initial value
        optionq = OptionMenu(masteru, var1, *case_year)
        optionq.grid(row=1,column=3,sticky=W,columnspan=2,padx=(10,0))
        
        
        loginbutton=Button(masteru,text="DELETE",command=casenos_window,fg="white",bg="green",font=("Helvetica", 14))
        loginbutton.grid(row=2,column=2)
        submitbutton=Button(masteru,text="GO BACK",command=closed_window,fg="white",bg="green",font=("Helvetica", 16))
        submitbutton.grid(row=2,column=3)


def casenos_window():
    
    pqw=var.get()
    pwq=var1.get()
    qwer=e1.get()
    convar = sqlite3.connect('case.db')
    query="DELETE FROM casedetails where cwp = ? and nmbr =? and year = ?"
    
    cursor = convar.execute(query,(pqw,qwer,pwq,))
   
    convar.commit()
    numaffectedrows = convar.total_changes
    convar.close()
    if numaffectedrows > 0:
        tkMessageBox.showinfo("CONGRATULATIONS!!!", "DELETE SUCCESSFULLY!!")
        closed_window()
    else:
        tkMessageBox.showinfo("OHOOOO!!!", "DELETE UNSUCCESSFUL!!")
        closed_window()


def filenos_window():
    
    s=e1.get()
    convar = sqlite3.connect('case.db')
    query="DELETE FROM casedetails where fn = ?"
    
    cursor = convar.execute(query,(s,))
   
    convar.commit()
    numaffectedrows = convar.total_changes
    convar.close()
    if numaffectedrows > 0:
        tkMessageBox.showinfo("CONGRATULATIONS!!!!", "DELETE SUCCESSFULLY!!")
        closed_window()
    else:
        tkMessageBox.showinfo("OHOOOOO!!!", "DELETE UNSUCCESSFUL!!")
        closed_window()


        
            

        
     

    






global masteru,back_image
masteru = Tk()
masteru.resizable(width=False, height=False)
masteru.geometry('900x695')
back_image=PhotoImage(file="brt.gif")
label=Label(masteru,image=back_image)
label.place(x=0, y=0, relwidth=1, relheight=1)


decision=["File no","Case no"]
var2 = StringVar()           #dec. a String var
var2.set("Search by")  # set initial initial value
optione = OptionMenu(masteru, var2, *decision,command=decisions)
optione.grid(row=1,column=0,sticky=W,padx=(80,0))
