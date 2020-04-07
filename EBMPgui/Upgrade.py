import Database
import Homepage
import Rules
from tkinter import*
from tkinter import messagebox
import WindowInitializing

def start(root,name):
    newPassword=StringVar()
    oldPassword=StringVar()
    title=Label(root,text="Upgrade Password",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)

    login_frame=Frame(root,bg="white")
    login_frame.place(x=400,y=150)

    passlbl = Label(login_frame, text="New Password",imag=root.password_icon,compound=LEFT,font=("times new roman", 30, "bold")).grid(row=1, column=1, padx=20, pady=10)
    passtxt = Entry(login_frame, bd=5,show="*",textvariable=newPassword, relief=GROOVE, font=("", 15)).grid(row=1, column=2, padx=20)
    oldPasslbl = Label(login_frame, text="Old Password",imag=root.password_icon,compound=LEFT, font=("times new roman", 30, "bold")).grid(row=2, column=1, padx=20,pady=10)
    oldPasstxt = Entry(login_frame, bd=5, show="*", textvariable=oldPassword, relief=GROOVE, font=("", 15)).grid(row=2,column=2,padx=20)
    btn_upgrade= Button(login_frame,text="Upgrade",width=20,command=lambda :upgradefun(root,name,newPassword,oldPassword),font=("times new roman",18,"bold"),bg="black",fg="white").grid(row=3,columnspan=2,pady=10)
    create_account = Button(login_frame, text="Back", width=20, command=lambda: change(root,name), font=("times new roman", 18, "bold"),bg="black", fg="white").grid(row=4, columnspan=2, pady=10)

def change(root,name):
    root.destroy()
    Homepage.homepage1(name)

def upgradefun(root,name, newPassword,oldPassword):
    var=newPassword.get()
    result=Rules.passwordVerification(var)

    if result==0:
        var = Database.upgradePassword(name, newPassword, oldPassword)

    if var ==1:
        messagebox.showinfo("Success","Upgraded Successfully")
        root.destroy()
        Homepage.homepage1(name)
    else:
        messagebox.showerror("Error","Failed")

def callme(name):
    root = WindowInitializing.window()
    start(root,name)
    root.mainloop()