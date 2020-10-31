#!/usr/bin/env python
# coding: utf-8

# In[35]:


from tkinter import*
from tkinter import ttk,messagebox
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Laxmi$9$",database="management")
mcrs=con.cursor()
root=Tk()
from PIL import Image,ImageTk
class register():
    def __init__(self,root):
         
        self.root=root
        self.root.title("home page")
        self.root.geometry("1350x700+0+0")
        self.bg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root)
        frame.place(x=100,y=100,width=500,height=500)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//supervisor.jpg")
        fbg=Label(frame,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        btn_sel=Button(frame,text="supervisor",bg="green",cursor="hand2",command=self.proff).place(x=100,y=420,width=180)
        title=Label(frame,text="supervisor",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
       
        frame0=Frame(self.root)
        frame0.place(x=700,y=100,width=500,height=500)
        self.fbg9=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//student.jpg")
        fbg9=Label(frame0,image=self.fbg9).place(x=0,y=0,relwidth=1,relheight=1)
        btn_sel=Button(frame0,text="student",bg="green",cursor="hand2",command=self.student).place(x=100,y=420,width=180)
        title=Label(frame0,text="student portal",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        
    
    def proff(self):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
         
        
        ##### BG right image ######
        
        self.bg1=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg1=Label(self.root,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)
        
        ##### left image #####
        
        #self.left=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpubg2.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        
        ###   register frame ####
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        fbg=Label(frame1,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(frame1,text="REGISTER HERE(supervisor)",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
         
        f_name=Label(frame1,text="name",font=("times new roman",15,"bold"),bg="white", fg="black").place(x=50,y=100)
        self.txt_name=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_name.place(x=50,y=130,width=250)
         
          #########
        contact=Label(frame1,text="CONTACT",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_contact.place(x=50,y=200,width=250)
        id=Label(frame1,text="ID",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_id=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_id.place(x=370,y=200,width=250)
        ########
        cource=Label(frame1,text="Department",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.cmb_course=ttk.Combobox(frame1,font=("times new roman",13)) 
        self.cmb_course['values']=("select","cse","ece","civil","mechanical")
        self.cmb_course.place(x=50,y=270,width=250)
        self.cmb_course.current(0)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_email.place(x=370,y=270,width=250)
            ########
        pwd=Label(frame1,text="Passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_pwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_pwd.place(x=50,y=340,width=250)
        Cpwd=Label(frame1,text="confirm passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_Cpwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_Cpwd.place(x=370,y=340,width=250)
            ######## terms ####
        btn_reg=Button(frame1,text="REGISTER",bg="green",cursor="hand2",command=self.register_data2).place(x=50,y=420)
        btn_login=Button(frame1,text="Login",bg="green",cursor="hand2",command=self.login_window1).place(x=500,y=420,width=180)
        #btn_hm=Button(frame1,text="home",bg="green",cursor="hand2",command=self.root).place(x=250,y=420,width=180)
         
    def register_data2(self):
        if self.txt_name.get()==""  or self.txt_contact.get()=="" or self.txt_id.get()=="" or self.cmb_course.get()=="select" or self.txt_email.get()=="" or self.txt_pwd.get()=="" or self.txt_Cpwd.get()=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        elif  self.txt_pwd.get() != self.txt_Cpwd.get():
            messagebox.showerror("error","confirm passward is wrong",parent=self.root)
        
        else:
                
            mcrs.execute("insert into supervisor1 (name,contact,id,course,email,passward,cpwd) values(%s,%s,%s,%s,%s,%s,%s)",(self.txt_name.get(),self.txt_contact.get(), self.txt_id.get(),self.cmb_course.get(),self.txt_email.get(), self.txt_pwd.get(), self.txt_Cpwd.get()))
            con.commit()
                 
            messagebox.showinfo("success","registered successfully",parent=self.root)

 
    def login_window1(self):
        
        self.root=root
        self.root.title("login form")
        self.root.geometry("1350x700+0+0")
        
        
        left=Label(self.root,bg="black",bd=0)
        left.place(x=0,y=0,relheight=1,width=600)
        
        right=Label(self.root,bg="green",bd=0)
        right.place(x=600,y=0,relheight=1,width=1)
        self.bg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        login_frm=Frame(self.root,bg="white")
        login_frm.place(x=250,y=100,height=500,width=800)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpubg2.jpg")
        fbg=Label(login_frm,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        title=Label(login_frm,text="login here",font=("times new roman",30,"bold"),fg="Black").place(x=50,y=30)
        id=Label(login_frm,text="Id number:",font=("times new roman",15,"bold"),bg="grey",fg="white").place( x=50,y=170)
        self.txt_id=Entry(login_frm,font=("times new roman",15),bg="lightgrey") 
        self.txt_id.place(x=250,y=170,width=350)
        pswd=Label(login_frm,text="passward:",font=("times new roman",15,"bold"),bg="grey",fg="white").place( x=150,y=280)
        self.txt_pswd=Entry(login_frm,font=("times new roman",15),bg="lightgrey") 
        self.txt_pswd.place(x=250,y=280,width=250)
        btn_reg=Button(login_frm,text="new register here",bg="green",command=self.proff,cursor="hand2").place(x=50,y=420)
        btn_login=Button(login_frm,text="LOGIN",command=self.login1,bg="green",cursor="hand2").place(x=250,y=360)
        #enterbtn=Button(login_frm, text="enter",command=self.details).place( x=150, y=360 )
         
     
        
    def login1(self):
        
        if self.txt_id.get()=="" or self.txt_pswd.get=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        else:
            mcrs.execute("select * from supervisor1 where id=%s and passward=%s ",(self.txt_id.get(),self.txt_pswd.get()))
            row=mcrs.fetchone()
            rows=row
        
            if rows==None:
                messagebox.showerror("error","invalid username and passward",parent=self.root)
        
            else:
                messagebox.showinfo("successfull","welcome", parent=self.root)
                self.details()
         
        
        
        
        
        
    def student(self):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
        #self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        #fbg=Label(frame1,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        ##### BG right image ######
        
        self.bg1=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg1=Label(self.root,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)
        
        ##### left image #####
        
        #self.left=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpubg2.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        
        ###   register frame ####
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        fbg=Label(frame1,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(frame1,text="REGISTER HERE(student)",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
         
        f_name=Label(frame1,text="FIRSTname",font=("times new roman",15,"bold"),bg="white", fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_fname.place(x=50,y=130,width=250)
        l_name=Label(frame1,text="LASTname",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_lname.place(x=370,y=130,width=250)
          #########
        contact=Label(frame1,text="CONTACT",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_contact.place(x=50,y=200,width=250)
        register=Label(frame1,text="Registration No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_register=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_register.place(x=370,y=200,width=250)
        ########
        cource=Label(frame1,text="COURSE",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.cmb_course=ttk.Combobox(frame1,font=("times new roman",13)) 
        self.cmb_course['values']=("select","cse","ece","civil","mechanical")
        self.cmb_course.place(x=50,y=270,width=250)
        self.cmb_course.current(0)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_email.place(x=370,y=270,width=250)
            ########
        pwd=Label(frame1,text="Passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_pwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_pwd.place(x=50,y=340,width=250)
        Cpwd=Label(frame1,text="confirm passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_Cpwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_Cpwd.place(x=370,y=340,width=250)
            ######## terms ####
        btn_reg=Button(frame1,text="REGISTER",bg="green",cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(frame1,text="Login",bg="green",cursor="hand2",command=self.login_window).place(x=500,y=420,width=180)
         
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_register.get()=="" or self.cmb_course.get()=="select" or self.txt_email.get()=="" or self.txt_pwd.get()=="" or self.txt_Cpwd.get()=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        elif  self.txt_pwd.get() != self.txt_Cpwd.get():
            messagebox.showerror("error","confirm passward is wrong",parent=self.root)
        
        else:
                
            mcrs.execute("insert into students1 (fname,lname,contact,registration,course,email,passward,cpwd) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(), self.txt_register.get(),self.cmb_course.get(),self.txt_email.get(), self.txt_pwd.get(), self.txt_Cpwd.get()))
            con.commit()
                 
            messagebox.showinfo("success","registered successfully",parent=self.root)

 
    
    def login_window(self):
        
        self.root=root
        self.root.title("login form")
        self.root.geometry("1350x700+0+0")
        
        
        left=Label(self.root,bg="black",bd=0)
        left.place(x=0,y=0,relheight=1,width=600)
        
        right=Label(self.root,bg="green",bd=0)
        right.place(x=600,y=0,relheight=1,width=1)
        self.bg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        login_frm=Frame(self.root,bg="white")
        login_frm.place(x=250,y=100,height=500,width=800)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpubg2.jpg")
        fbg=Label(login_frm,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        title=Label(login_frm,text="login here",font=("times new roman",30,"bold"),fg="Black").place(x=50,y=30)
        reg=Label(login_frm,text="registration number:",font=("times new roman",15,"bold"),bg="grey",fg="white").place( x=50,y=170)
        self.txt_reg=Entry(login_frm,font=("times new roman",15),bg="lightgrey") 
        self.txt_reg.place(x=250,y=170,width=350)
        pswd=Label(login_frm,text="passward:",font=("times new roman",15,"bold"),bg="grey",fg="white").place( x=150,y=280)
        self.txt_pswd=Entry(login_frm,font=("times new roman",15),bg="lightgrey") 
        self.txt_pswd.place(x=250,y=280,width=250)
        btn_reg=Button(login_frm,text="new register here",bg="green",command=self.student,cursor="hand2").place(x=50,y=420)
        btn_login=Button(login_frm,text="LOGIN",command=self.login,bg="green",cursor="hand2").place(x=250,y=360)
        #enterbtn=Button(login_frm, text="enter",command=self.details).place( x=150, y=360 )
         
     
        
    def login(self):
        
        if self.txt_reg.get()=="" or self.txt_pswd.get=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        else:
            mcrs.execute("select * from students1 where registration=%s and passward=%s ",(self.txt_reg.get(),self.txt_pswd.get()))
            row=mcrs.fetchone()
            rows=row
        
            if rows==None:
                messagebox.showerror("error","invalid username and passward",parent=self.root)
        
            else:
                messagebox.showinfo("successfull","welcome", parent=self.root)
                #self.details()
         
               
  
    def details(self):
                          
        self.root=root
        self.root.title("LPU student management")
        self.root.geometry("1370x700+0+0")
        
        #self.bg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        #bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(self.root,text="Lpu student management",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="white",fg="black")
        title.pack()
        
        self.reg_no_var=StringVar()
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.contact_var=StringVar()
        self.course_var=StringVar()
        self.email_var=StringVar()
        self.passward_var=StringVar()
        self.cpwd_var=StringVar()
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        manage_frame.place(x=600,y=100,width=658,height=585)
        
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        detail_frame.place(x=20,y=100,width=558,height=585)
        
        n_title=Label(manage_frame,text="Student Details",font=("times new roman",30,"bold"),bg="white",fg="green")
        n_title.grid(row=0,columnspan=2,pady=20,padx=100)
        
        lbl_reg=Label(manage_frame,text="Registration no",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_reg.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_reg=Entry(manage_frame,textvariable=self.reg_no_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_reg.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(manage_frame,text="First name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(manage_frame,textvariable=self.fname_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(manage_frame,text="Last name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_name.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(manage_frame,textvariable=self.lname_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_contact=Label(manage_frame,text="Contact",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_contact.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lbl_course=Label(manage_frame,text="Course",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_course.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        combo_course= ttk.Combobox(manage_frame,textvariable=self.course_var,font=("times new roman",11,"bold"),state='readonly')
        combo_course['values']=("CSE","ECE","Mech","Civil")
        combo_course.grid(row=5,column=1,pady=10,padx=20,sticky="w" )
        
        lbl_email=Label(manage_frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_email.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_pswd=Label(manage_frame,text="Passward",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_pswd.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        txt_pswd=Entry(manage_frame,textvariable=self.passward_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_pswd.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        lbl_cpwd=Label(manage_frame,text="confirm Passward",font=("times new roman",15,"bold"),bg="white",fg="black")
        lbl_cpwd.grid(row=8,column=0,pady=10,padx=20,sticky="w" )
        txt_cpwd=Entry(manage_frame,textvariable=self.cpwd_var,font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_cpwd.grid(row=8,column=1,pady=10,padx=20,sticky="w" )
        bckbtn=Button(manage_frame,text="back",width=10,command=self.login_window1,bg="green").grid(row=9,column=4,padx=10,pady=10)
        
        btn_frame=Frame(manage_frame,bd=3,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=525,width=428)
        
        addbtn=Button(btn_frame,text="Add",command=self.student2,width=10).grid(row=0,column=0,padx=10,pady=10)
        updtbtn=Button(btn_frame,text="Update",command=self.update,width=10).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clbtn=Button(btn_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        combo_search = ttk.Combobox(detail_frame,width=10,font=("times new roman",12,"bold"),state='readonly')
        combo_search ['values']=("search by","Reg no","first name","course")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="w" )
        
        txt_search=Entry(detail_frame,font=("times new roman",11,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=0,sticky="w")
        
        srchbtn=Button(detail_frame,text="Search",width=10).grid(row=1,column=2,padx=10,pady=10)
        
        Table_frm=Frame(detail_frame,bd=4,relief=RIDGE,bg="white")
        Table_frm.place(x=10,y=100,width=530,height=450)
        
        scroll_x=Scrollbar(Table_frm,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frm,orient=VERTICAL)
        self.student_table=ttk.Treeview(Table_frm,columns=("fname","lname","contact","reg_no","course","email" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("reg_no",text="reg_no")
        self.student_table.heading("fname",text="firstName")
        self.student_table.heading("lname",text="lastName")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("email",text="Email")
        
        self.student_table['show']='headings' 
        self.student_table.column("reg_no",width=100)
        self.student_table.column("fname",width=100)
        self.student_table.column("lname",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("course",width=50)
        self.student_table.column("email",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.fetch)
        self.show()
        
    
    def student2(self):
        self.root=root
        self.root.title("Registration form")
        self.root.geometry("1350x700+0+0")
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
        #self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        #fbg=Label(frame1,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        
        ##### BG right image ######
        
        self.bg1=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        bg1=Label(self.root,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)
        
        ##### left image #####
        
        #self.left=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpubg2.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        
        ###   register frame ####
        frame1=Frame(self.root)
        frame1.place(x=480,y=100,width=700,height=500)
        self.fbg=ImageTk.PhotoImage(file="C:/Users/Satya Chowdary/Downloads//lpu1.jpg")
        fbg=Label(frame1,image=self.fbg).place(x=0,y=0,relwidth=1,relheight=1)
        
        title=Label(frame1,text="REGISTER HERE(student)",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
         
        f_name=Label(frame1,text="FIRSTname",font=("times new roman",15,"bold"),bg="white", fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_fname.place(x=50,y=130,width=250)
        l_name=Label(frame1,text="LASTname",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_lname.place(x=370,y=130,width=250)
          #########
        contact=Label(frame1,text="CONTACT",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_contact.place(x=50,y=200,width=250)
        register=Label(frame1,text="Registration No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_register=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_register.place(x=370,y=200,width=250)
        ########
        cource=Label(frame1,text="COURSE",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        self.cmb_course=ttk.Combobox(frame1,font=("times new roman",13)) 
        self.cmb_course['values']=("select","cse","ece","civil","mechanical")
        self.cmb_course.place(x=50,y=270,width=250)
        self.cmb_course.current(0)
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_email.place(x=370,y=270,width=250)
            ########
        pwd=Label(frame1,text="Passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_pwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_pwd.place(x=50,y=340,width=250)
        Cpwd=Label(frame1,text="confirm passward",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_Cpwd=Entry(frame1,font=("times new roman",15),bg="lightgrey") 
        self.txt_Cpwd.place(x=370,y=340,width=250)
            ######## terms ####
        btn_reg=Button(frame1,text="REGISTER",bg="green",cursor="hand2",command=self.register_data3).place(x=50,y=420)
        btn_login=Button(frame1,text="back",bg="green",cursor="hand2",command=self.details).place(x=500,y=420,width=180)
         
    def register_data3(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_register.get()=="" or self.cmb_course.get()=="select" or self.txt_email.get()=="" or self.txt_pwd.get()=="" or self.txt_Cpwd.get()=="":
            messagebox.showerror("error","All feilds are required",parent=self.root)
        elif  self.txt_pwd.get() != self.txt_Cpwd.get():
            messagebox.showerror("error","confirm passward is wrong",parent=self.root)
        
        else:
                
            mcrs.execute("insert into students1 (fname,lname,contact,registration,course,email,passward,cpwd) values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(), self.txt_register.get(),self.cmb_course.get(),self.txt_email.get(), self.txt_pwd.get(), self.txt_Cpwd.get()))
            con.commit()
                 
            messagebox.showinfo("success","registered successfully",parent=self.root)

 
    def show(self):
        mcrs.execute("select * from students1")
        rows=mcrs.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.reg_no_var.set("") 
        self.fname_var.set("") 
        self.lname_var.set("")  
        self.contact_var.set("")  
        self.course_var.set("")  
        self.email_var.set("")  
        self.passward_var.set("")  
        self.cpwd_var.set("") 
    def fetch(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.fname_var.set(row[0])
        self.lname_var.set(row[1])
        self.reg_no_var.set(row[3])
        self.contact_var.set(row[2])
        self.course_var.set(row[4])
        self.email_var.set(row[5])
        #self.passward_var.set(row[6])
        #self.cpwd_var.set(row[END,7])
        con.commit()
    def update(self):
        
        mcrs.execute("update students1 set fname=%s,lname=%s,contact=%s,course=%s,email=%s,passward=%s,cpwd=%s where registration=%s",(self.fname_var.get(),self.lname_var.get(),self.contact_var.get(),self.course_var.get(),self.email_var.get(), self.passward_var.get(),self.cpwd_var.get()))
        con.commit()
        self.show()
        self.clear()
        self.fetch()
        messagebox.showinfo("success","updated")
    
    
            
   
 
     
        
            
obj=register(root)  


root.mainloop()
 


# In[ ]:





# In[ ]:




