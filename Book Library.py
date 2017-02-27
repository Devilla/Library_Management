from Tkinter import *
from tkMessageBox import *
import sqlite3
conn=sqlite3.Connection(":memory:")

conn.text_factory = str

cur=conn.cursor()
root=Tk()
a = PhotoImage(file="Kids.gif")
#below line will add image only in the screen
w1 = Label(root, image=a).pack(side="top")
root.attributes("-fullscreen",True)



cur.execute("create table lib(book_id number, book varchar (20), Author varchar (20), copies number, Publication varchar (30))")
cur.execute("insert into lib values(1425,'Sherlock Holmes','Conan Doyle',20,'Vintage Publications')")
cur.execute("insert into lib values(1215,'Think Python','E. Rilley',200,'S.S. Publications')")
cur.execute("insert into lib values(1245,'Harry Potter','J.K. ROWLING',20,'McGrawHill Publications')")
cur.execute("insert into lib values(4125,'3 Mistakes of my life','Chetan Bhagat',200,'S.S. Publications')")
cur.execute("create table name(book_id number,username varchar (20), pass varchar (20), email varchar (40))")
cur.execute("insert into name values(0,'DEV','raju','abc@gmail.com')")
#cur.execute("create table futsal(boo varchar (20), Auth varchar (20)")
#books={"LOVE STORY", "HATE STORY"}
#cur.execute("insert into futsal values(books,'Conan Doyle')")
sql3 = "SELECT * FROM futsal"
sql = "SELECT username FROM name WHERE username = ?"
sql2 = "SELECT pass FROM name WHERE pass = ?"
'''def footy():
            for row in cur.execute(sql3,):
                ab=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
footy()'''
def login():
    root=Tk()
   # b = PhotoImage(file="Kids2.gif")
    #below line will add image only in the screen
    #w2=Label(root, image=b).pack(side="top")
    root.attributes("-fullscreen",True)

    shortcutbar30 = Frame(root, height=1, bg='light blue')
    toolbar30 = Label(shortcutbar30, text='Please Login to continue..',bg='orange',fg='black',height=4,font='TIMES 20 italic bold ')
    toolbar30.pack(side=TOP,fill=X)
    shortcutbar30.pack(fill=X)

    x = StringVar()
    y = StringVar()
    
    shortcutbar31 = Frame(root, height=30, bg='orange')
    toolbar31 = Label(shortcutbar31, text='Username',bg='orange',fg='black',height=4,font='TIMES 18 italic bold')
    toolbar31.pack(side=TOP,fill=X)
    e6 = Entry(shortcutbar31,textvariable=x)
    e6.pack(side=TOP)
    shortcutbar31.pack(fill=X)

    shortcutbar32 = Frame(root, height=1, bg='orange')
    toolbar32 = Label(shortcutbar32, text='Password',bg='orange',fg='black',height=4,font='TIMES 18 italic bold')
    toolbar32.pack(side=TOP,fill=X)
    e7 = Entry(shortcutbar32, show='*',textvariable=y)
    e7.pack(side=TOP)  
    shortcutbar32.pack(fill=X)
    Label(root, text = " ",bg='orange').pack(side=TOP,anchor=CENTER,fill=X)

    def close():
        us=str(e6.get())
        ps=str(e7.get())
        def Error1():
            if(str(e6.get())==''or str(e7.get())==''):
                s=showerror(title="ERROR",message="Fill the entries")
        Error1()
        def Error2():
            if(str(us)!='DEV' or str(ps)!='raju'):
                s=showerror(title="ERROR",message="WRONG ENTRIES!!  Try Again....")
        Error2()       
            
        def readData():
            for row in cur.execute(sql, [(us)]):
                ab=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",","")) 
            for row in cur.execute(sql2, [(ps)]):
                ab2=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))     
                if(ab==us or ab2==ps):
                    root4=Tk()
                    root4.attributes("-fullscreen",True)

                    def displayall2():
                        root5=Tk()
                        sql3="select username from name"
                        for row in cur.execute(sql3,):
                            ab2=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
                            Label(root5, text = ab2 ).pack()
                            Label(root5, text = '(ADMIN)').pack()
                            #b=cur.fetchall()
                            #Label(root4,text=b).pack()
                            #w=OptionMenu(root,"book1","book2","book3",b)
                            #w.pack(side=TOP)
                    def displayall():
                        root6=Tk()
                        sql4="select book  from lib "
                        for row in cur.execute(sql4):
                            ab3=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",",""))
                            Label(root6,text=ab3).pack()
                                #w=OptionMenu(root6,"BOOK1",ab3)
                                #w.pack(side=TOP)
                    def issue_book():
                        root7=Tk()
                        sql5="select book  from lib where Author = 'Conan Doyle'"
                        for row in cur.execute(sql5):
                            ab5=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",","")) 
                            Label(root7,text=ab5).pack()
                            def click():
                                Label(root7,text="Your Book Has Been Issued.").pack()
                                sql51="update book_id= ? where Author = 'Conan Doyle'"
                                for row in cur.execute(sql5):
                                    ab5=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",","")) 
                                    Label(root7,text='Book Details: ').pack()
                                    Label(root7,text='Book : ').pack()
                                    Label(root7,text=ab5).pack()
                                sql6="select Author  from lib where Author = 'Conan Doyle'"
                                for row in cur.execute(sql6):
                                    ab6=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",","")) 
                                    Label(root7,text='Author :').pack()
                                    Label(root7,text=ab6).pack()
                                sql7="select Publication from lib where Author = 'Conan Doyle'"
                                for row in cur.execute(sql7):
                                    ab7=(str(row).replace(')','').replace('(','').replace('u\'','').replace("'","").replace(",","")) 
                                    Label(root7,text='Publication House:').pack()
                                    Label(root7,text=ab7).pack()

                            Button(root7, text='Click to issue', command = click,bg='light blue',fg='black',font='Times 12 bold ').pack()

                    shortcutbar9=Frame(root4,height=30)
                    toolbar=Label(shortcutbar9, text=" WELCOME ",font="-weight bold",bg="blue",height=3)
                    toolbar.pack(side=TOP,fill=X)
                    shortcutbar9.pack(fill=X)     
                    Button(root4, text='ISSUE BOOK', command = issue_book,bg='light blue',fg='black',font='Times 10 bold ',height=2,bd=4).pack(side=TOP,anchor=NW)
                    shortcutbar911=Frame(root4,height=30)
                    toolbar11=Label(shortcutbar911, text="",font="-weight bold")
                    toolbar11.pack(side=TOP,fill=X)
                    shortcutbar911.pack(fill=X)
                    Button(root4, text='Display Books', command = displayall,bg='light blue',fg='black',font='Times 10 bold ',height=2,bd=4).pack(side=TOP,anchor=NW)
                    shortcutbar912=Frame(root4,height=30)
                    toolbar12=Label(shortcutbar912, text="",font="-weight bold")
                    toolbar12.pack(side=TOP,fill=X)
                    shortcutbar912.pack(fill=X)
                    Button(root4, text='Display USERS', command = displayall2,bg='light blue',fg='black',font='Times 10 bold',height=2,bd=4).pack(side=TOP,anchor=NW)
                    shortcutbar91=Frame(root4,height=30)
                    toolbar1=Label(shortcutbar91, text="",font="-weight bold")
                    toolbar1.pack(side=TOP,fill=X)
                    shortcutbar91.pack(fill=X)
                    def close4():
                        root4.destroy()
                    Button(root4, text='BACK ', command = close4,bg='light blue',fg='black',font='Times 10 bold',height=2,bd=4).pack(side=BOTTOM,fill=X)
                    def rules():
                        root4=Tk()
                        root4.title("NEW BOOK ADDITION")
                        shortcutbar1=Frame(root4,height=30)
                        Label(shortcutbar1, text="ADD NEW BOOK DETAILS",bg="green").pack(side=TOP,anchor=NW)
                        shortcutbar1.pack(side=TOP)
                        m = StringVar()
                        n = StringVar()
                        o = StringVar()
                        p = StringVar()
                        q = StringVar()
                        am = StringVar()
                        bm = StringVar()
                        cm = StringVar()
                        dm = StringVar()
                        vairable=StringVar()
                        shortcutbar=Frame(root4,height=30)
                        Label(shortcutbar, text="Book Name : ").pack(side=TOP,anchor=NW,expand=NO)
                        e1 = Entry(shortcutbar, textvariable=m)
                        e1.pack(side=TOP)

                        Label(shortcutbar, text="BOOK ID : " ).pack(side=TOP,anchor=NW,expand=NO)
                        e5 = Entry(shortcutbar, textvariable=q)     
                        e5.pack(side=TOP,anchor=NW)
                        shortcutbar.pack(side=TOP)
                        
                        Label(shortcutbar, text="Author : ").pack(side=TOP,anchor=NW,expand=NO)
                        e2 = Entry(shortcutbar, textvariable=n)
                        e2.pack(side=TOP)
                        Label(shortcutbar, text="Copies : " ).pack(side=TOP,anchor=NW,expand=NO)
                        e3 = Entry(shortcutbar, textvariable=o)
                        e3.pack(side=TOP,anchor=NW)
                        Label(shortcutbar, text="Publication House : " ).pack(side=TOP,anchor=NW,expand=NO)
                        e4 = Entry(shortcutbar, textvariable=p)     
                        e4.pack(side=TOP,anchor=NW)
                        shortcutbar.pack(side=TOP)
                        def info():
                                
                            am=e1.get()
                            bm=e2.get()
                            cm=e3.get()
                            dm=e4.get()
                            em=e4.get()
                            tupp=(em,am,bm,cm,dm)
                            def Error1():
                                if(str(e1.get())==''or str(e2.get())==''or str(e3.get())==''or str(e4.get())=='' or str(e5.get())==''):
                                    s=showerror(title="ERROR",message="Fill the entries")
                            Error1()
                            def disp():
                                cur.execute("insert into lib values(?,?,?,?,?)",tupp)
                                conn.commit()
                                root4.destroy()
                            Button(root4, text='save', command = disp ).pack(side=TOP,anchor=SW)    
                        Button(root4, text='OK!!', command = info,height=1,width=6).pack(side=TOP,anchor=SW)
                        root4.bind('<Return>',info) 
                    Button(root4, text='ADD NEW BOOK', command = rules,bg='light blue',fg='black',font='Times 10 bold',height=2,bd=4).pack(side=TOP,anchor=NW)


        readData()         
        


    def close5():
            root.destroy()
    
    shortcutbar312 = Frame(root, height=10, bg='green')
    toolbar312 = Label(shortcutbar312,text='',bg='orange',height=4)
    toolbar312.pack(fill=X)
    shortcutbar312.pack(fill=X)


    def close2(event=0):
        close()
        root.destroy()
    root.bind('<Return>', close2)
    shortcutbar317 = Frame(root, height=1, bg='orange')
    toolbar317 = Button(shortcutbar317,text='Submit',command=close2,bg='sky blue',fg='black',height=1,font='TIMES 16 italic bold')
    toolbar317.pack()
    shortcutbar317.pack(fill=X)
    shortcutbar315 = Frame(root, height=10, bg='green')
    toolbar315 = Label(shortcutbar315,text='',bg='orange',height=4)
    toolbar315.pack(fill=X)
    shortcutbar315.pack(fill=X)
    shortcutbar3123 = Frame(root, height=10, bg='green')
    toolbar3123 = Label(shortcutbar3123,text='',bg='orange',height=4)
    toolbar3123.pack(fill=X)
    shortcutbar3123.pack(fill=X)
    
    shortcutbar316 = Frame(root, height=10, bg='green')
    toolbar316 = Label(shortcutbar316,text='',bg='orange',height=4)
    toolbar316.pack(fill=X)
    shortcutbar316.pack(fill=X)
    shortcutbar323 = Frame(root, height=1, bg='orange')
    toolbar323 = Button(shortcutbar323,text='BACK',command=close5,bg='sky blue',fg='black',height=1,font='TIMES 16 italic bold')
    toolbar323.pack(side=LEFT,anchor=SW)
    shortcutbar323.pack(fill=X)
    
def exitmain():
    root.destroy()
        
def new_user():
    
    root2=Tk()
    root2.attributes("-fullscreen",True)
    shortcutbar = Frame(root2, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='SIGN UP !',bg='orange',fg='black',height=4,font='TIMES 18 italic bold underline')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root2,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root2,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root2,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root2,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    q = StringVar()
    r = StringVar()
    s = StringVar()
    door=Frame(root2, height=10, bg='sky blue')
    toolbar=Label(root2, text = "Username ",bg='sky blue')
    toolbar.pack(side=TOP)
    door.pack(side=TOP)
    e1 = Entry(root2, textvariable=q,bg='sky blue')
    e1.pack(side=TOP)
    Label(root2, text="Password ",bg='green').pack(side=TOP)
    e2 = Entry(root2,show='*', textvariable=r,bg='green')
    e2.pack(side=TOP)
    Label(root2, text="Email ID  ",bg='yellow').pack(side=TOP)
    e3 = Entry(root2, textvariable=s,bg='yellow')
    e3.pack(side=TOP)
    def info2():

        
        j=e1.get()
        k=e2.get()
        l=e3.get()
        bill=(0,j,k,l)


        def disp2():
                
            cur.execute("insert into name values(?,?,?,?)",bill)
            save=conn.commit()
            shortcutbar121 = Frame(root, height=60, bg='orange')
            Label(root2, text='Your Profile is created !',fg='black',font='Times 12 bold').pack(side=BOTTOM,fill=X,anchor=SW)
            shortcutbar121.pack(expand=NO, fill=X)
            print 

 
        Button(root2, text='SUBMIT', command = disp2 ).pack(side=TOP)
    Button(root2, text='ok', command = info2 ).pack(side=TOP)
    def close3(event=0):
        root2.destroy()
    root2.bind('<Return>', close3)
    shortcutbar121 = Frame(root, height=60, bg='orange')
    Button(root2, text='Back To Main Page', command = close3,bg='light blue',fg='black',font='Times 12 bold').pack(side=BOTTOM,fill=X,anchor=SW)
    shortcutbar121.pack(expand=NO, fill=X)
    
def aboutus():
    master=Tk()
    master.attributes("-fullscreen",True)
    shortcutbar = Frame(master, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='PYTHON PROJECT',bg='light green',fg='purple',height=4,font='TIMES 18 italic bold underline')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
    shortcutbar1=Frame(master,height=30)
    toolbar1=Label(shortcutbar1, text='LIBRARY MANAGEMENT \n PROJECT DEVELOPED BY:',fg='black',font='Times 18')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(fill=X)
    shortcutbar2=Frame(master,height=30)
    toolbar2=Label(shortcutbar2, text='Devender (141211)',fg='black',font='Times 20 bold')
    toolbar2.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar2.pack(fill=X)
    shortcutbar3=Frame(master,height=30)
    toolbar3=Label(shortcutbar3, text='\nFACULTY INCHARGE:',fg='black',font='Times 18')
    toolbar3.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar3.pack(fill=X)
    shortcutbar4=Frame(master,height=30)
    toolbar4=Label(shortcutbar4, text='Dr. Mahesh Kumar',fg='black',font='Times 20 bold')
    toolbar4.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar4.pack(fill=X)
    
    def sbmt():
        master.destroy()
        page2()
    s = Frame(master, height=30, bg='light green')
    Button(s,text='CLOSE',width=16,height=2,bd=4,bg='light blue',fg='black',font='Times 12 bold',command=master.destroy).pack(side=BOTTOM,fill=X,anchor=SW)
    s.pack(expand=NO,fill=X,side=BOTTOM)
    
shortcutbar2 = Frame(root, height=60, bg='orange')
toolbar = Label(shortcutbar2, text="Welcome To Library",bg='orange',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar2.pack(expand=NO, fill=X)

shortcutbar3 = Frame(root, height=60, bg='orange')
toolbar2 = Label(shortcutbar3, text="BOOK A BEAUTIFUL BOOK TODAY!!!",bg='orange',fg='black',height=2,font='CalibriLight 12 bold')
toolbar2.pack(side=TOP,expand=NO)
shortcutbar3.pack(expand=NO, fill=X)
shortcutbar1=Frame(root, height=60, bg='orange')
toolbar1 = Button(shortcutbar1, text='LOGIN!', command = login,bg='orange',fg='black',font='Times 12 bold ',bd=4)
toolbar1.pack(side=TOP,expand=NO,anchor=W)
shortcutbar1.pack(expand=NO, fill=X)
shortcutbar4 = Frame(root, height=60, bg='blue')
toolbar = Label(shortcutbar4, text="",bg='orange',fg='black',height=2,font='CalibriLight 12 bold')
toolbar.pack(side=TOP,fill=X,expand=YES)
shortcutbar4.pack(expand=NO, fill=X)
shortcutbar = Frame(root, height=60, bg='orange')
toolbar = Button(shortcutbar, text='SIGN UP!', command = new_user,bg='orange',fg='black',font='Times 12 bold',bd=4)
toolbar.pack(side=TOP,expand=NO,anchor=W)
shortcutbar.pack(expand=NO, fill=X)
'''shortcutbar12 = Frame(root, height=60, bg='orange')
Button(root, text='About Us', command = aboutus,bg='light blue',fg='black',font='Times 12 bold').pack(side=BOTTOM,fill=X,anchor=SW)
shortcutbar12.pack(expand=NO, fill=X)'''
shortcutbar12 = Frame(root, height=60, bg='orange')
Button(root, text='EXIT', command = exitmain,bg='light blue',fg='black',font='Times 12 bold').pack(side=BOTTOM,fill=X,anchor=SW)
shortcutbar12.pack(expand=NO, fill=X)

root.mainloop()
