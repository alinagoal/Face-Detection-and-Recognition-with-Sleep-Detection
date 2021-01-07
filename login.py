from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk
import random
import time
import datetime
import os

class Login_System:
	def __init__(self, root):
 		
 		self.root=root
 		self.root.title("Login Page")
 		self.root.geometry("1350x700+0+0")

 		self.bg_icon=ImageTk.PhotoImage(file="images/backy.jpg")
 		self.user_icon=PhotoImage(file="images/user1.png")
 		self.pass_icon= PhotoImage(file="images/pass1.png")
 		self.logo_icon= PhotoImage(file="images/logo1.png")

 		self.uname=StringVar()
 		self.pass_=StringVar()

 		bg_lbl=Label(self.root,image=self.bg_icon).pack()

 		title=Label(self.root,text="Login System",font=("Arial Narrow", 30,"bold"),bg="#A15A4B",fg="#F0E211" ,relief=GROOVE)
 		title.place(x=0,y=0,relwidth=1)



 		Login_Frame = Frame(self.root,bg="white")
 		Login_Frame.place(x=400,y=150)

 		logolbl=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=20)
 		
 	
 		lbluser =Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("Arial Narrow", 17 , "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
 		txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)


 		lblpass =Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("Arial Narrow", 17 , "bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)
 		txtpass=Entry(Login_Frame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("",15),show='*').grid(row=2,column=1,padx=20)

 		btn_log =Button(Login_Frame,text="Login",width=15,command=self.login,font=("Arial Narrow", 14, "bold"),bg="#A15A4B",fg="#F0E211").place( x=30,y=337)

 		btn_reset=Button(Login_Frame,text="Reset",width=15,command=self.reset,font=("Arial Narrow", 14, "bold"),bg="#A15A4B",fg="#F0E211").grid( row=3,column=1, pady=10)


	def login(self):
 		if (self.uname.get())=="Alilum" and (self.pass_.get())=="123456":
 			
 			os.system("python train.py")
 			
 		elif (self.uname.get())=="" or (self.pass_.get())=="":
 			ms.showerror("Error", "All fields are required!!")
 		else:
 			ms.showerror("Error","Invalid Username or Password")


	def reset(self):
 		self.uname.set("")
 		self.pass_.set("")
 		


root=Tk()
obj=Login_System(root)
root.mainloop()

