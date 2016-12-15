from tkinter import *
import sqlite3


from tkinter import messagebox as tkMessageBox
def update_window():
    a1k=e111.get()
    a2k=var9.get()
    a3k=e2.get()
    a4k=var10.get()
    a5k=e3.get()
    a6k=e4.get()
    a7k=e5.get()
    a8k=e6.get()
    a9k=e7.get()
    a10k=e8.get()
    a11k=var82.get()
    a12k=e10.get()
    a13k=e11.get()
    a14k=e12.get()
    a15k=e13.get()
    
    convar = sqlite3.connect('case.db')
    query='''UPDATE casedetails set fn = ? ,cwp = ? ,nmbr = ? ,year = ?,pn = ? ,noc = ? ,df = ?,dp = ?,status = ?,type = ? ,fp = ? ,afd = ? ,email = ? ,phoneno = ?,otherdetail= ? where cwp = ? and nmbr = ? and year = ? '''

    convar.execute(query,(a1k,a2k,a3k,a4k,a5k,a6k,a7k,a8k,a9k,a10k,a11k,a12k,a13k,a14k,a15k,a2k,a3k,a4k))
    convar.commit()
    
    numaffectedrows = convar.total_changes
    convar.close()




    if numaffectedrows > 0:
        tkMessageBox.showinfo("CONGRATULATIONS!!!", "UPDATE SUCCESSFULLY!!")
        closed_window()
    else:
        tkMessageBox.showinfo("OHOOOOO!!!", "UPDATE UNSUCCESSFUL!!")
        closed_window()
    

def closed_window():
    
    koot.destroy()
    exec(open("mainpage1.py").read())
   
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=870,height=550)


def decisions(se):
    
    global option,fileno_window,update_window,casenos_window,filenos_window,noc_window,pname_window,type_window,status_window,feepaid_window
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



    
def filenos_window():
    global frame,e111,e2,e3,e4,e5,e6,e7,e8,var82,var9,var10,e10,e11,e12,e13
    for widget in frame.winfo_children():
        widget.destroy()
    
    qwers=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where fn = ?"
    
    cursor = convar.execute(query,(qwers,))


    w1 = Label(frame, text="FILE NO ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w1.grid(row=0,column=0,sticky=W,pady=(0,5))
    e111 = Entry(frame,font=("Comic Sans MS", 14))
    e111.grid(row=0, column=1)

    w2 = Label(frame, text="CASE NO ",fg="black",font=("Comic Sans MS", 14))
    w2.grid(row=1,column=0,sticky=W,pady=(0,5))


    case_type=["CWP","CRM-M","CR","RSA","CRR","CRA-S","FAO","CM","CRM","ARB","CA","CACP","CAPP","CCEC","CCES","CEA","CEC","CEGC","CESR","CLAIM","CMA","CMM","CO","COA","COCP","CP","CRA","CRA-AD","CRA-AS","CRA-D","CRACP","CREF","CRM-A","CRM-W","CROCP","CRR(F)","CRREF","CRWP","CS","CS-OS","CUSAP","DP","EA","EDC","EDREF","EFA","EP","ESA","FAO(FC)","FAO-C","FAO-M","GCR","GSTR","GTA","GTC","GTR","GVATR","INCOMP","INTTA","IOIN","ITA","ITC","ITR","LPA","LR","MATRF","MRC","O&M","OLR","PBT","PVR","RA","RA-CA","RA-CP","RA-CR","RA-CW","RA-LP","RA-RF","RA-RS","RCRWP","RFA","RP","SA","SAO","SDR","STA","STC","STR","TA","TC","TCRM","UVA","UVR","VATAP","VATCASE","VATREF","WTA","WTC","WTR","XOBJ","XOBJC","XOBJL","XOBJR","XOBJS","OTHER"]
    var9 = StringVar()           #dec. a String var
    var9.set("Case Type")  # set initial initial value
    option = OptionMenu(frame, var9, *case_type)
    option.grid(row=1,column=1,sticky=W,padx=55)


    e2 = Entry(frame,font=("Comic Sans MS", 14))
    e2.grid(row=1, column=1,sticky=E,padx=160,columnspan=2)


    case_year=["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
    var10 = StringVar()           #dec. a String var
    var10.set("Case Year")  # set initial initial value
    optionq = OptionMenu(frame, var10, *case_year)
    optionq.grid(row=1,column=2,sticky=W,columnspan=2,padx=(10,0))



    w3 = Label(frame, text=" PARTIES NAME ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w3.grid(row=2,column=0,sticky=W,pady=(0,5))
    e3 = Entry(frame,font=("Comic Sans MS", 14))
    e3.grid(row=2, column=1)


    w4 = Label(frame, text="NAME OF OPPOSITE COUNSEL",fg="black",font=("Comic Sans MS", 14))
    w4.grid(row=3,column=0,sticky=W,padx=(0,10),pady=(0,5))
    e4 = Entry(frame,font=("Comic Sans MS", 14))
    e4.grid(row=3, column=1)


    w5 = Label(frame, text="DATE FIXED",fg="black",bg='White',font=("Comic Sans MS", 14))
    w5.grid(row=4,column=0,sticky=W,pady=(0,5))
    e5 = Entry(frame,font=("Comic Sans MS", 14))
    e5.grid(row=4, column=1)


    w6 = Label(frame, text="DATE PENDING",fg="black",font=("Comic Sans MS", 14))
    w6.grid(row=5,column=0,sticky=W,pady=(0,5))
    e6 = Entry(frame,font=("Comic Sans MS", 14))
    e6.grid(row=5, column=1)

    w7 = Label(frame, text="STATUS",fg="black",bg='White',font=("Comic Sans MS", 14))
    w7.grid(row=6,column=0,sticky=W,pady=(0,5))
    e7 = Entry(frame,font=("Comic Sans MS", 14))
    e7.grid(row=6, column=1)

    w8 = Label(frame, text="TYPE",fg="black",font=("Comic Sans MS", 14))
    w8.grid(row=7,column=0,sticky=W,pady=(0,5))
    e8 = Entry(frame,font=("Comic Sans MS", 14))
    e8.grid(row=7, column=1)


    w9 = Label(frame, text="FEE PAID",fg="black",bg='White',font=("Comic Sans MS", 14))
    w9.grid(row=8,column=0,sticky=W,pady=(0,5))
    decision=["YES","NO","NONE"]
    var82 = StringVar()           #dec. a String var
    var82.set("Fee Paid?")  # set initial initial value
    optione = OptionMenu(frame, var82, *decision)
    optione.grid(row=8,column=1,sticky=W,padx=(80,0))



    w10 = Label(frame, text="ADDITIONAL FEE DETAILS ",fg="black",font=("Comic Sans MS", 14))
    w10.grid(row=9,column=0,sticky=W,pady=(0,5))
    e10 = Entry(frame,font=("Comic Sans MS", 14))
    e10.grid(row=9, column=1)


    w11 = Label(frame, text="EMAIL ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w11.grid(row=10,column=0,sticky=W,pady=(0,5))
    e11 = Entry(frame,font=("Comic Sans MS", 14))
    e11.grid(row=10,column=1)


    w12 = Label(frame, text="PHONE NO ",fg="black",font=("Comic Sans MS", 14))
    w12.grid(row=11,column=0,sticky=W,pady=(0,5))
    e12 = Entry(frame,font=("Comic Sans MS", 14))
    e12.grid(row=11, column=1)


    w13 = Label(frame, text="OTHER DETAILS",fg="black",bg='White',font=("Comic Sans MS", 14))
    w13.grid(row=12,column=0,sticky=W,pady=(0,5))
    e13 = Entry(frame,font=("Comic Sans MS", 14))
    e13.grid(row=12, column=1)


    w13 = Label(frame,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
    w13.grid(row=13,column=0,columnspan=3,sticky=W,pady=(0,0))











    for row in cursor:
        e111.insert(END,row[0])
        
        var9.set(row[1])
        var10.set(row[3])
        
        var82.set(row[10])
        e2.insert(END,row[2])
        e3.insert(END,row[4])
        e4.insert(END,row[5])
        e5.insert(END,row[6])
        e6.insert(END,row[7])
        e7.insert(END,row[8])
        e8.insert(END,row[9])
        e10.insert(END,row[11])
        e11.insert(END,row[12])
        e12.insert(END,row[13])
        e13.insert(END,row[14])
    submitbutton=Button(frame,text="UPDATE",command=update_window,fg="white",bg="green",font=("Helvetica", 16))
    submitbutton.grid(row=14,column=1,columnspan=2,sticky=W)


    w13 = Label(frame,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
    w13.grid(row=15,column=0,columnspan=3,sticky=W,pady=(0,0))



    convar.commit()
     

    convar.close()



    
def casenos_window():
    global frame,e111,e2,e3,e4,e5,e6,e7,e8,var82,var9,var10,e10,e11,e12,e13
    for widget in frame.winfo_children():
        widget.destroy()
    
    pqw=var.get()
    pwq=var1.get()
    qwer=e1.get()
    convar = sqlite3.connect('case.db')
    query="SELECT fn,cwp,nmbr,year,pn,noc,df,dp,status,type,fp,afd,email,phoneno,otherdetail FROM casedetails where cwp = ? and nmbr = ? and year = ?"
    
    cursor = convar.execute(query,(pqw,qwer,pwq,))


    w1 = Label(frame, text="FILE NO ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w1.grid(row=0,column=0,sticky=W,pady=(0,5))
    e111 = Entry(frame,font=("Comic Sans MS", 14))
    e111.grid(row=0, column=1)

    w2 = Label(frame, text="CASE NO ",fg="black",font=("Comic Sans MS", 14))
    w2.grid(row=1,column=0,sticky=W,pady=(0,5))


    case_type=["CWP","CRM-M","CR","RSA","CRR","CRA-S","FAO","CM","CRM","ARB","CA","CACP","CAPP","CCEC","CCES","CEA","CEC","CEGC","CESR","CLAIM","CMA","CMM","CO","COA","COCP","CP","CRA","CRA-AD","CRA-AS","CRA-D","CRACP","CREF","CRM-A","CRM-W","CROCP","CRR(F)","CRREF","CRWP","CS","CS-OS","CUSAP","DP","EA","EDC","EDREF","EFA","EP","ESA","FAO(FC)","FAO-C","FAO-M","GCR","GSTR","GTA","GTC","GTR","GVATR","INCOMP","INTTA","IOIN","ITA","ITC","ITR","LPA","LR","MATRF","MRC","O&M","OLR","PBT","PVR","RA","RA-CA","RA-CP","RA-CR","RA-CW","RA-LP","RA-RF","RA-RS","RCRWP","RFA","RP","SA","SAO","SDR","STA","STC","STR","TA","TC","TCRM","UVA","UVR","VATAP","VATCASE","VATREF","WTA","WTC","WTR","XOBJ","XOBJC","XOBJL","XOBJR","XOBJS","OTHER"]
    var9 = StringVar()           #dec. a String var
    var9.set("Case Type")  # set initial initial value
    option = OptionMenu(frame, var9, *case_type)
    option.grid(row=1,column=1,sticky=W,padx=55)


    e2 = Entry(frame,font=("Comic Sans MS", 14))
    e2.grid(row=1, column=1,sticky=E,padx=160,columnspan=2)


    case_year=["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
    var10 = StringVar()           #dec. a String var
    var10.set("Case Year")  # set initial initial value
    optionq = OptionMenu(frame, var10, *case_year)
    optionq.grid(row=1,column=2,sticky=W,columnspan=2,padx=(10,0))



    w3 = Label(frame, text=" PARTIES NAME ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w3.grid(row=2,column=0,sticky=W,pady=(0,5))
    e3 = Entry(frame,font=("Comic Sans MS", 14))
    e3.grid(row=2, column=1)


    w4 = Label(frame, text="NAME OF OPPOSITE COUNSEL",fg="black",font=("Comic Sans MS", 14))
    w4.grid(row=3,column=0,sticky=W,padx=(0,10),pady=(0,5))
    e4 = Entry(frame,font=("Comic Sans MS", 14))
    e4.grid(row=3, column=1)


    w5 = Label(frame, text="DATE FIXED",fg="black",bg='White',font=("Comic Sans MS", 14))
    w5.grid(row=4,column=0,sticky=W,pady=(0,5))
    e5 = Entry(frame,font=("Comic Sans MS", 14))
    e5.grid(row=4, column=1)


    w6 = Label(frame, text="DATE PENDING",fg="black",font=("Comic Sans MS", 14))
    w6.grid(row=5,column=0,sticky=W,pady=(0,5))
    e6 = Entry(frame,font=("Comic Sans MS", 14))
    e6.grid(row=5, column=1)

    w7 = Label(frame, text="STATUS",fg="black",bg='White',font=("Comic Sans MS", 14))
    w7.grid(row=6,column=0,sticky=W,pady=(0,5))
    e7 = Entry(frame,font=("Comic Sans MS", 14))
    e7.grid(row=6, column=1)

    w8 = Label(frame, text="TYPE",fg="black",font=("Comic Sans MS", 14))
    w8.grid(row=7,column=0,sticky=W,pady=(0,5))
    e8 = Entry(frame,font=("Comic Sans MS", 14))
    e8.grid(row=7, column=1)


    w9 = Label(frame, text="FEE PAID",fg="black",bg='White',font=("Comic Sans MS", 14))
    w9.grid(row=8,column=0,sticky=W,pady=(0,5))
    decision=["YES","NO","NONE"]
    var82 = StringVar()           #dec. a String var
    var82.set("Fee Paid?")  # set initial initial value
    optione = OptionMenu(frame, var82, *decision)
    optione.grid(row=8,column=1,sticky=W,padx=(80,0))



    w10 = Label(frame, text="ADDITIONAL FEE DETAILS ",fg="black",font=("Comic Sans MS", 14))
    w10.grid(row=9,column=0,sticky=W,pady=(0,5))
    e10 = Entry(frame,font=("Comic Sans MS", 14))
    e10.grid(row=9, column=1)


    w11 = Label(frame, text="EMAIL ",fg="black",bg='White',font=("Comic Sans MS", 14))
    w11.grid(row=10,column=0,sticky=W,pady=(0,5))
    e11 = Entry(frame,font=("Comic Sans MS", 14))
    e11.grid(row=10,column=1)


    w12 = Label(frame, text="PHONE NO ",fg="black",font=("Comic Sans MS", 14))
    w12.grid(row=11,column=0,sticky=W,pady=(0,5))
    e12 = Entry(frame,font=("Comic Sans MS", 14))
    e12.grid(row=11, column=1)


    w13 = Label(frame, text="OTHER DETAILS",fg="black",bg='White',font=("Comic Sans MS", 14))
    w13.grid(row=12,column=0,sticky=W,pady=(0,5))
    e13 = Entry(frame,font=("Comic Sans MS", 14))
    e13.grid(row=12, column=1)


    w13 = Label(frame,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
    w13.grid(row=13,column=0,columnspan=3,sticky=W,pady=(0,0))











    for row in cursor:
        e111.insert(END,row[0])
        
        var9.set(row[1])
        var10.set(row[3])
        
        var82.set(row[10])
        e2.insert(END,row[2])
        e3.insert(END,row[4])
        e4.insert(END,row[5])
        e5.insert(END,row[6])
        e6.insert(END,row[7])
        e7.insert(END,row[8])
        e8.insert(END,row[9])
        e10.insert(END,row[11])
        e11.insert(END,row[12])
        e12.insert(END,row[13])
        e13.insert(END,row[14])
    submitbutton=Button(frame,text="UPDATE",command=update_window,fg="white",bg="green",font=("Helvetica", 16))
    submitbutton.grid(row=14,column=1,columnspan=2,sticky=W)


    w13 = Label(frame,text="                                                                                                                                                                                                                                                                                                                 ",bg="brown")
    w13.grid(row=15,column=0,columnspan=3,sticky=W,pady=(0,0))



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





decision=["File no","Case no"]
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


myscrollbar=Scrollbar(roots,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)


