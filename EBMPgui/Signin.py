import Database
import Homepage
import Signup
from tkinter import*
from tkinter import messagebox
import WindowInitializing


class Geek:
    def getVal(self):
        return name



def change(root):
    root.destroy()
    Signup.Call(root)

def change_case(event=None):
    messagebox.showerror("Error", "Enter Valid Data")

global name
def login(root, username, password):
    global name
    name=username.get()
    myresult=Database.verifyUser(username,password)

    if len(myresult) >= 1:
        root.destroy()
        Homepage.homepage1(name)
    else:
        messagebox.showerror("Error","Enter Valid Data")
def name():
    return name
def Start(root):
    Label(root, image=root.bg_icon_signin).pack()
    username = StringVar()
    password = StringVar()

    #title = Label(root, text="Login", font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10,relief=GROOVE)
   # title.place(x=0, y=0, relwidth=1)

    #logolbl= Label(root,image=root.login_icon,bd=4, bg="black")
    #logolbl.place(in_=title, relx=0.45, rely=2 )

    #lbluser = Label(root, text="Username", compound=LEFT, fg="blue", bg="grey",
                    #font=("times new roman", 20, "bold")).place(in_=title, relx=0, rely=1.5)
    txtuser = Entry(root, textvariable=username, bd=2, relief=GROOVE,width=30, font=("", 18)).place(x=225,
                                                                                           y=270)
    #lbluser = Label(root, text="Password", compound=LEFT, fg="blue", bg="grey",font=("times new roman", 20, "bold")).place(in_=title, relx=0, rely=2.2)
    txtpassword = Entry(root, textvariable=password, show="*", bd=2,width=30, relief=GROOVE, font=("", 18)).place(
                                                                                                         x=225,
                                                                                                         y=370)
    btn_login = Button(root, text="Login", width=15,height=1, command=lambda: login(root,username,password),
                       font=("times new roman", 12,"bold"), bg="#BBBAAA", fg="#FAF9F3").place( x=340,
                                                                                           y=440)

    #lblforgotPassword = Label(root, text="Forgotton Password?", compound=LEFT, fg="red", bg="black",
                              #font=("times new roman", 18, "bold"))
    #lblforgotPassword.bind("<Button-1>", change_case)
    #lblforgotPassword.place(in_=title, relx=0.7, rely=2.2)
    create_account = Button(root, text="Create new account",width=15, command=lambda: change(root),
    font=("times new roman", 12, "bold"), bg="#E55B8D", fg='white').place(x=740,y=520)

def call():
    root=WindowInitializing.window()
    Start(root)
    root.mainloop()