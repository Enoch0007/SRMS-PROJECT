from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3 as db 

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        width= self.root.winfo_screenwidth()               
        height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (width, height))
        self.root.config(bg="light blue")   

        title=Label(self.root,text="Thakur College of Science and Commerce",compound=LEFT,padx=20,font=("goudy old style",30,"bold"),bg="orange",fg="blue").place(x=0,y=0,relwidth=1,height=50)


        #--Bg Image--
        #self.bg=ImageTk.PhotoImage(file="C:/Users/enoch/Documents/login python/Images/register.jpg")
        #bg=Label(self.root,image=self.bg).place(x=0,y=0)

        #--Register Frame--
        frame1=Frame(self.root,bg="lightyellow")
        frame1.place(x=400,y=150,width=700,height=500)

        title=Label(frame1,text="REGISTERE HERE",font=("times new roman",20,"bold"),bg="lightyellow",fg="Blue").place(x=50,y=30)

        #-------Row1-----------------
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_lname.place(x=370,y=130,width=250)

        #-------------Row2----------
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_email.place(x=370,y=200,width=250)
    
        #-----Row3------------------
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new romans",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_answer.place(x=370,y=270,width=250)
        

        #-------------Row4----------
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="lightyellow",fg="black").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new romans",15),bg="white")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #-------Terms---------
        self.var_chk=IntVar()       
        chk=Checkbutton(frame1,text="I Agree to the Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",13,"bold"),bg="lightyellow",fg="black").place(x=50,y=380)

        btn_register=Button(frame1,text="REGISTER NOW",font=("times new romans",13,"bold"),bg="blue",fg="white",cursor="hand2",command=self.register_data).place(x=50,y=430)
        btn_signin=Button(frame1,text="SIGN IN",command=self.login_window,font=("times new romans",13,"bold"),bg="blue",fg="white",cursor="hand2").place(x=370,y=430)

    
    def login_window(self):
        self.root.destroy()

        import login
    
    
    
    
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.delete(0)
    
    
    
    def register_data(self): 
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password does not Match",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree with our Terms and Coditions",parent=self.root)
        else:
            try:
                con=db.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User already Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))       
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                self.clear()            
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

root=Tk()
obj=Register(root)
root.mainloop()
