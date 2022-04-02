
import tkinter as tk,mysql.connector as con


class a(tk.Frame):
       def info1(self,p,c):
            tk.Frame.__init__(self,p)
            self.configure(bg="green")
            n=tk.Label(self,text="Database",font=("Arial",25,"bold"),bd=2,bg="cyan")
            n.place(x=530,y=0)
            item=tk.Label(self,text="item",font=("Helvatica",15),bd=2,padx=10)
            item.place(x=400,y=120)
            item_e=tk.Entry(self)
            item_e.place(x=560,y=120)
            price=tk.Label(self,text="price",font=("Helvatica",15),bd=2,padx=10)
            price.place(x=400,y=180)
            price_e=tk.Entry(self)
            price_e.place(x=560,y=180)
            total=tk.Label(self,text="add money",font=("Helvatica",15),bd=2,padx=10)
            total.place(x=400,y=240)
            total_e=tk.Entry(self)
            total_e.place(x=560,y=240)
            
      
            mydb=con.connect(host="localhost",user=l[0],password=l[1])
            mycon=mydb.cursor()
            import datetime as d
            m=d.datetime.now().strftime("%B")
            try:
              x=f"use l[0]"
              mycon.execute(x)
            except:
                   
                    
                    ec=f"create database if not exists {l[0]}"
                    mycon.execute(ec) 
                    x=f"use {l[0]}"        #has to be update
                   
                    mycon.execute(x)
            import datetime as d
            m=d.datetime.now().strftime("%B")
            tat=f"create table if not exists {m} (item varchar(100),price varchar(100),date varchar(100),total varchar(100))"
            mycon.execute(tat)
            
            month=f"select * from {m}"
            mycon.execute(month)
            data=mycon.fetchall()                               
            jj=list(data)
            global tota
            try:
              
              zz=list(jj[-1])
              tota=str(zz[-1])         
            except:
                
                tota=0  
            smoney1=tk.Label(self,text="Total money",font=("Helvatica",15),bd=2,padx=10)
            smoney2=tk.Label(self,text=tota,font=("Helvatica",15),bd=2,padx=10)
            smoney1.place(x=750,y=60)
            smoney2.place(x=920,y=60)

            mydb.commit()
            def bac():
                     c.nn(cc)
                     

            back=tk.Button(self,text="back",cursor="hand2",font=("Helvatica",12),bd=2,command=bac)
            back.place(x=750,y=300)
            mydb.commit()
            def done():
                  y=f"use {l[0]}"
                  mycon.execute(y)
                  import datetime as d
                  m=d.datetime.now().strftime("%B")
                  ta=f"create table if not exists {m} (item varchar(100),price varchar(100),date varchar(100),total varchar(100))"
                  mycon.execute(ta)
                  o=f"insert into {m} values (%s,%s,%s,%s)"
                  ii=d.datetime.now()
                  date=ii.strftime("%d")+"-"+ii.strftime("%m")+"-"+ii.strftime("%y")
                  tttt=total_e.get()
                  price=price_e.get()
                  if tttt=="":
                                  tttt=0
                  if price=="":
                                  price=0                
                  rem=str(int(tota)-int(price))
                
                  if(int(rem)<0):
                        from tkinter import messagebox as m
                        m.showerror("error","insufficient balance!!")
                  else:      
                        
                            
                       vv=item_e.get(),price,date,str(int(rem)+int(tttt))
                       mycon.execute(o,vv)
                       mydb.commit()
            b=tk.Button(self,text="commit",font=("Helvatica",15),bd=2,command=done)
            b.place(x=450,y=300)


class mysqll(tk.Frame):
   
       def info(self,p,c):
            global l
            l=[]
            
            tk.Frame.__init__(self,p)     
           # self.configure(bg="blue")          #  mydb=con.connect(host="localhost",user="jugal",password="Jugal2002@")
            l11=tk.Label(self,text="Mysql Authentication",font=("Arial",25,"bold"),bd=2,bg="cyan")
            l11.place(x=413,y=0)
            l22=tk.Label(self,text="username",font=("Helvatica",15))
            l22.place(x=430,y=120)
            e22=tk.Entry(self)
            e22.place(x=560,y=120)
            l33=tk.Label(self,text="password",font=("Helvatica",15))
            l33.place(x=430,y=180)
            e33=tk.Entry(self)
            e33.place(x=560,y=180)
            self.user=e22.get()
            self.password=e33.get()
            def newacc():
                         self.user=e22.get()
                         self.password=e33.get()
                         
                         
                         try:
                           import os
                           os.system("service mysql start")
                           mydb=con.connect(host="localhost",user=self.user,password=self.password)
                           l.append(self.user)
                           l.append(self.password)
                           
                           c.nn(cc)
                         except:
                              from tkinter import messagebox as m

                              m.showerror("Authentication error","incorrect username and password")  
            new=tk.Button(self,text="sign in",cursor="hand2",font=("Helvatica",12),bd=2,command=newacc)
            new.place(x=440,y=240)
            
          
class b(tk.Frame):
       def compute(self,p,c):
                                        
            tk.Frame.__init__(self,p)
           # self.configure(bg="cyan")
           
            global pp
            
            def ok():
                  global user,l2
                  l2=[]
                  user=e2.get()
              
                  p1=e3.get()
                  cd=mysqll()
                  mydb=con.connect(host="localhost",user=l[0],password=l[1])
                  mycon=mydb.cursor()
                  mycon.execute("create database if not exists password_data")
                  mycon.execute("use password_data")
                  mycon.execute("create table if not exists data (username varchar(100) primary key,password varchar(100))")
                  mycon.execute("select * from data")
                  data=mycon.fetchall()
                  
                  store={}                                           
                  mycon.execute("select * from data")
 
                  jj=list(data)
                  for k in jj:
                     zz=list(k)
                     store[zz[0]]=zz[1]
                  from tkinter import messagebox as m 
                  found=0
                  if len(store)==0:
                          m.showerror("alert","user not found!!")    
                  for k in range(len(store)):
                    if user in store:
                      if store[user]==p1:
                             
                  
                               mydb=con.connect(host="localhost",user=l[0],password=l[1])
                               mycon=mydb.cursor()
                               l2.append(user)
                               h=f"create database if not exists {e2.get()}"
                               mycon.execute(h)
                               f=a()
                               
                               f.info1(p,c)
                               #c.nn(a)
                               f.grid(row=0,column=0,sticky="nsew")
                               f.tkraise()
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
                         mydb=con.connect(host="localhost",user=l[0],password=l[1])
                         mycon=mydb.cursor()
                         mycon.execute("create database if not exists password_data")
                         mycon.execute("use password_data")
                         mycon.execute("create table if not exists data (username varchar(100) primary key,password varchar(100))")
                         if e22.get()!="" and e33.get()!="":
                           h="insert into data values(%s,%s)"
                           hh=e22.get(),e33.get()
                           mycon.execute(h,hh)
                          
                         mydb.commit()
                         c.nn(b) 
                         
            new=tk.Button(self,text="sign up",cursor="hand2",font=("Helvatica",12),bd=2,command=create)
            new.place(x=700,y=240)
            def leave():
                   c.nn(b)
            exit=tk.Button(self,text="Already have an account",cursor="hand2",font=("Helvatica",12),bd=2,command=leave)
            exit.place(x=450,y=240)
    
                     
                                      
            
class d(tk.Tk):
       def __init__(self):
            tk.Tk.__init__(self)
            w=tk.Frame(self)
            w.pack(expand=True)
            w.grid_rowconfigure(0,minsize=580)
            w.grid_columnconfigure(0,minsize=1200)
         
            f1=b()
            f1.compute(w,self)
            f1.grid(row=0,column=0,sticky="nsew")
             
            d=mysqll()
            d.info(w,self)
            d.grid(row=0,column=0,sticky="nsew")
            f=a()

      #      f.grid(row=0,column=0,sticky="nsew")
            
            f2=cc(w,self)
            f2.grid(row=0,column=0,sticky="nsew")
          
            self.geometry("1370x800")
            self.resizable(False,False)
            self.h={b:f1,a:f,cc:f2,mysqll:d}      
            self.configure(bg="yellow")
            self.nn(mysqll)
       def nn(self,v):
            m=self.h[v]
            m.grid(row=0,column=0,sticky="nsew")
            m.tkraise()


try:
   c=d()
   c.maxsize(1370,800)
   c.mainloop()
except:
       print("sorry, unable to access mysql server")     
