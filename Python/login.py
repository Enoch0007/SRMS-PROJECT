from cgitb import reset
import email
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3 as db
import os

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        width= self.root.winfo_screenwidth()               
        height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (width, height))
        self.root.config(bg="light blue")   

        title=Label(self.root,text="Thakur College of Science and Commerce",compound=LEFT,padx=20,font=("goudy old style",30,"bold"),bg="orange",fg="blue").place(x=0,y=0,relwidth=1,height=50)

        #----Frame------
        frame1=Frame(self.root,bg="lightyellow")
        frame1.place(x=400,y=150,width=700,height=500)

        title=Label(frame1,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="lightyellow",fg="Blue").place(x=230,y=30)

        email=Label(frame1,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="lightyellow",fg="black").place(x=230,y=130)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="white",fg="black")
        self.txt_email.place(x=230,y=170,width=350,height=35)

        password=Label(frame1,text="PASSWORD",font=("times new roman",18,"bold"),bg="lightyellow",fg="black").place(x=230,y=230)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="white",fg="black")
        self.txt_password.place(x=230,y=270,width=350,height=35)

        btn_reg=Button(frame1,text="Register New Accout",command=self.register_window,font=("times new roman",15),bg="lightyellow",bd=0,fg="blue",cursor="hand2").place(x=230,y=315)

        btn_forget=Button(frame1,text="Forget Password?",command=self.forget_password_window,font=("times new roman",15),bg="lightyellow",bd=0,fg="blue",cursor="hand2").place(x=430,y=315)

        
        btn_login=Button(frame1,text="LOGIN",command=self.login,font=("times new roman",20,"bold"),bg="orange",fg="white",cursor="hand2").place(x=290,y=380,width=180,height=40)

        
        #----Image-- 
        self.bg_image=Image.open("Images/admin.png")
        self.bg_image=self.bg_image.resize((225,300),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_image,bg="lightyellow").place(x=400,y=250)

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)
    
    
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=db.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=? ",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select the Current Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","your password has been reset,Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)
    
    
    
    
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the  email to reset your password",parent=self.root)
        else:
            try:
                con=db.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email to reset your password",parent=self.root)
                    
                else:

                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x400+600+200")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="blue").place(x=0,y=10,relwidth=1)

                    #----Forget password----
                    question=Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=120,y=100)
                
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new romans",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=80,y=130,width=250)
                    self.cmb_quest.current(0)
                
                    answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=160,y=180)
                    self.txt_answer=Entry(self.root2,font=("times new romans",15),bg="white")
                    self.txt_answer.place(x=80,y=210,width=250)
            
                    new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=140,y=260)
                    self.txt_new_password=Entry(self.root2,font=("times new romans",15),bg="white")
                    self.txt_new_password.place(x=80,y=290,width=250)
            
                    btn_change_password=Button(self.root2,text="Reset Password",command=self.forget_password,bg="orange",fg="white",font=("times new roman",15,"bold")).place(x=100,y=340)



            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)






    def register_window(self):
        self.root.destroy()
        import register
                



    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=db.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Email and Password",parent=self.root)
                    
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                
                
                con.close()
            except Exception as es:
                    messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)



root=Tk()
obj=Login_window(root)
root.mainloop()

