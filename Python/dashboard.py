from tkinter import*
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3 as db
class RMS:

    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management Software")
        width= self.root.winfo_screenwidth()               
        height= self.root.winfo_screenheight()               
        self.root.geometry("%dx%d" % (width, height))
        self.root.config(bg="white")

        #--icon-- 
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #--title--
        title=Label(self.root,text="Student Result Management Sofware",compound=LEFT,padx=20,image=self.logo_dash,font=("goudy old style",30,"bold"),bg="orange",fg="blue").place(x=0,y=0,relwidth=1,height=50)

        #--menu--
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white",fg="Black")
        M_Frame.place(x=10,y=60,width=1515,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_Student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.add_student).place(x=270,y=5,width=200,height=40)
        btn_Result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.add_result).place(x=520,y=5,width=200,height=40)
        btn_View=Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.add_report).place(x=770,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.logout).place(x=1020,y=5,width=200,height=40)
        btn_Exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="dark blue",fg="white",cursor="hand2",command=self.exit_).place(x=1270,y=5,width=200,height=40) 
        
        #--content window---
        self.bg_image=Image.open("images/bg.png")
        self.bg_image=self.bg_image.resize((1000,400),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_image).place(x=450,y=180,width=1000,height=400)
        
        
        #--update details--
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=450,y=600,width=300,height=100)

        self.lbl_Students=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_Students.place(x=800,y=600,width=300,height=100)
        
        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_result.place(x=1148,y=600,width=300,height=100)
       
         #--footer--
        footer=Label(self.root,text="SMRS- Student Result Management Sofware\nContact Us for any Tecnical Issue: 7666XXXX53 ",font=("goudy old style",20,),bg="black",fg="white").pack(side=BOTTOM,fill=X)
        self.update_course_details()
        self.update_student_details()
        self.update_result_details()


    def update_course_details(self):
        con=db.connect(database="rms.db")
        cur=con.cursor()

        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_course_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update_student_details(self):
        con=db.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_Students.config(text=f"Total Students\n[{str(len(cr))}]")
            self.lbl_Students.after(200,self.update_student_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def update_result_details(self):
        con=db.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            self.lbl_result.after(200,self.update_result_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

        


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

         



if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()

