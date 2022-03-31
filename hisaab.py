import tkinter as tk
class a(tk.Frame):
       def __init__(self,p,c):
            tk.Frame.__init__(self,p)
            self.configure(bg="green")
            n=tk.Label(self,text="Database",font=("Arial",25,"bold"),bd=2,bg="cyan")
            n.place(x=530,y=0)
            item=tk.Label(self,text="item",font=("Helvatica",15),bd=2,padx=10)
            item.place(x=430,y=120)
            item_e=tk.Entry(self)
            item_e.place(x=560,y=120)
            price=tk.Label(self,text="price",font=("Helvatica",15),bd=2,padx=10)
            price.place(x=430,y=180)
            price_e=tk.Entry(self)
            price_e.place(x=560,y=180)
            total=tk.Label(self,text="total",font=("Helvatica",15),bd=2,padx=10)
            total.place(x=430,y=240)
            total_e=tk.Entry(self)
            total_e.place(x=590,y=240)
            import mysql.connector as con
            mydb=con.connect(host="localhost",user="jugal",password="Jugal2002@")
            mycon=mydb.cursor()

           
            def done():
                  y=f"use {l[0]}"
                  mycon.execute(y)
                  import datetime as d
                  m=d.datetime.now().strftime("%B")
                  ta=f"create table if not exists {m} (item varchar(100),price varchar(100),date varchar(100),total varchar(100))"
                  mycon.execute(ta)
                  o=f"insert into {m} values (%s,%s,%s,%s)"
                  i=d.datetime.now()
                  date=i.strftime("%d")+"-"+i.strftime("%m")+"-"+i.strftime("%y")
                  vv=item_e.get(),price_e.get(),date,str(int(total_e.get())-int(price_e.get()))
                  mycon.execute(o,vv)
                  mydb.commit()
            b=tk.Button(self,text="commit",font=("Helvatica",15),bd=2,command=done)
            b.place(x=450,y=300)
global l        
l=[]
class b(tk.Frame):

       def __init__(self,p,c):
            tk.Frame.__init__(self,p)
           # self.configure(bg="cyan")
            global pp
            
            def ok():
                  global user
                  user=e2.get()
                  l.append(user)
                  p1=e3.get()
                  

                  import mysql.connector as con
                  mydb=con.connect(host="localhost",user="jugal",password="Jugal2002@")
                  mycon=mydb.cursor()
                  mycon.execute("use password_data")
                  mycon.execute("select * from data")
                  data=mycon.fetchall()
                  
                  store={}                                           
                  mycon.execute("select * from data")
 
                  jj=list(data)
                  for i in jj:
                     zz=list(i)
                     store[zz[0]]=zz[1]
                  from tkinter import messagebox as m 
                  found=0    
                  for i in range(len(store)):
                    if user in store:
                      if store[user]==p1:
                             rr=m.askquestion("user exist!!","Do you want to continue?")
                             if rr=="yes":
                               import mysql.connector as con
                               mydb=con.connect(host="localhost",user="jugal",password="Jugal2002@")
                               mycon=mydb.cursor()
                               h=f"create database if not exists {e2.get()}"
                               mycon.execute(h)
                               c.nn(a)
                      else:
                               found=1         
                    else:
                           m.showerror("Error","username not found!!")                
                  if found==1:
                               m.showerror("Error","incorrect password!!")                
            l1=tk.Label(self,text="Hisaab",font=("Arial",25,"bold"),bd=2,bg="cyan")
            l1.place(x=530,y=0)
            l2=tk.Label(self,text="username",font=("Helvatica",15))
            l2.place(x=430,y=120)
            e2=tk.Entry(self)
            e2.place(x=560,y=120)
            l3=tk.Label(self,text="password",font=("Helvatica",15))
            l3.place(x=430,y=180)
            e3=tk.Entry(self)
            e3.place(x=560,y=180)
            def newacc():
                         c.nn(cc)
            new=tk.Button(self,text="create a new account",cursor="hand2",font=("Helvatica",12),bd=2,command=newacc)
            new.place(x=420,y=240)
            sign=tk.Button(self,text="sign in",cursor="hand2",font=("Helvatica",12),bd=3,command=ok)
            sign.place(x=690,y=240)
            
class cc(tk.Frame):
        def __init__(self,p,c):
            tk.Frame.__init__(self,p)
            l11=tk.Label(self,text="Hisaab",font=("Arial",25,"bold"),bd=2,bg="cyan")
            l11.place(x=530,y=0)
            l22=tk.Label(self,text="username",font=("Helvatica",15))
            l22.place(x=430,y=120)
            e22=tk.Entry(self)
            e22.place(x=560,y=120)
            l33=tk.Label(self,text="password",font=("Helvatica",15))
            l33.place(x=430,y=180)
            e33=tk.Entry(self)
            e33.place(x=560,y=180)
            def create():
                         import mysql.connector as con
                         mydb=con.connect(host="localhost",user="jugal",password="Jugal2002@")
                         mycon=mydb.cursor()
                         mycon.execute("create database if not exists password_data")
                         mycon.execute("use password_data")
                         mycon.execute("create table if not exists data (username varchar(100) primary key,password varchar(100))")
                         h="insert into data values(%s,%s)"
                         hh=e22.get(),e33.get()
                         mycon.execute(h,hh)
                         mydb.commit()
                         c.nn(b) 
                         
            new=tk.Button(self,text="create account",cursor="hand2",font=("Helvatica",12),bd=2,command=create)
            new.place(x=620,y=240)
               
               
                                      
            
class d(tk.Tk):
       def __init__(self):
            tk.Tk.__init__(self)
            w=tk.Frame(self)
            w.pack(expand=True)
            w.grid_rowconfigure(0,minsize=580)
            w.grid_columnconfigure(0,minsize=1200)
            
            f=a(w,self)
            f.grid(row=0,column=0,sticky="nsew")
            
            f1=b(w,self)
            f1.grid(row=0,column=0,sticky="nsew")
            
            f2=cc(w,self)
            f2.grid(row=0,column=0,sticky="nsew")
            
            self.geometry("1370x800")
            self.resizable(False,False)
            self.h={b:f1,a:f,cc:f2}      
            self.configure(bg="yellow")
            f1.tkraise()
       def nn(self,v):
            m=self.h[v]
            m.grid(row=0,column=0,sticky="nsew")
            m.tkraise()

import os
try:
 os.system("service mysql start")
 c=d()
 c.maxsize(1370,800)
 c.mainloop()
except:
    print("mysql server not found!!")

