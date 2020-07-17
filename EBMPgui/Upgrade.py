import Database
import Homepage
import Rules
from tkinter import*
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
def showImage(self,photo):
    self.label2 = Label(image=photo, width=200, height=200)
    self.label2.image = photo
    self.label2.place(x=650, y=200)
def fileDialog(self,name):
    try:

        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg",".png"), ("all files", "*.*")))

        img = Image.open(self.filename)
        img = img.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        showImage(self,photo)

        insertBLOB(name,self.filename)
    except:
        messagebox.showerror("EBMP","Invalid type")

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(name,photo):
    print("Inserting BLOB into python_employee table")
    import actual.DataBaseConnect
    mydb, mycursor = actual.DataBaseConnect.database()
    try:

        cursor = mydb.cursor()
        sql_insert_blob_query = "UPDATE user SET Image = %s WHERE Username=%s"

        empPicture = convertToBinaryData(photo)

        # Convert data into tuple format
        insert_blob_tuple = (empPicture,name)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        mydb.commit()
        messagebox.showinfo("EBMP","Updated Successfully")

    except :
        messagebox.showerror("EBMP","Failed, Try Again")




def start(window,name):
    Label(window, image=window.bg_update).pack()
    import EBMPgui.Homepage
    image=EBMPgui.Homepage.readBLOB(window,name)
    if image!=None:
        showImage(window,image)
    #window.bg_update = ImageTk.PhotoImage(file=r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images\updatescreen.png")

    #label = Label(window, image=window.bg_update)
    #label.image = window.bg_update
    #label.pack()
    newPassword=StringVar()
    confirmNewPassword = StringVar()
    oldPassword=StringVar()
    #title=Label(window,text="Upgrade Password",font=("times new roman",40,"bold"),bg="black",fg="white",bd=20,relief=GROOVE)
    #title.place(x=0,y=0,relwidth=1)

    #login_frame=Frame(window,bg="white")
    #login_frame.place(x=400,y=150)
    oldPasstxt = Entry(window, bd=5, show="*", textvariable=oldPassword,width=20, font=("", 15)).place(x=230,y=230)
    #passlbl = Label(login_frame, text="New Password",imag=window.password_icon,compound=LEFT,font=("times new roman", 30, "bold")).grid(row=1, column=1, padx=20, pady=10)
    newpassword = Entry(window, bd=5,show="*",textvariable=newPassword,width=20, font=("", 15)).place(x=230,y=335)
    confirmnewPassword = Entry(window, bd=5, show="*", textvariable=confirmNewPassword,width=20 , font=("", 15)).place(x=230,y=435)
    #oldPasslbl = Label(login_frame, text="Old Password",imag=window.password_icon,compound=LEFT, font=("times new roman", 30, "bold")).grid(row=2, column=1, padx=20,pady=10)

    btn_upgrade= Button(window,text="Update Password",width=20,command=lambda :upgradefun(window,name,newPassword,confirmNewPassword,oldPassword),font=("times new roman", 12, "bold"), bg="#BBBAAA", fg="#FAF9F3").place(x=330,y=500)
    back = Button(window, image=window.back_icon, command=lambda: change(window,name)).place(x=200,y=85)
    button = Button(window, text="Browse Pic",font=("times new roman", 12, "bold"), bg="#BBBAAA", fg="#FAF9F3", command=lambda: fileDialog(window, name))
    button.place(x=700, y=450)
    window.mainloop()
def change(window,name):
    window.destroy()
    Homepage.homepage1(name)

def upgradefun(window,name,newPassword,confirmNewPassword,oldPassword):
    var=newPassword.get()
    var1=confirmNewPassword.get()

    if (var==var1):
        result=Rules.passwordVerification(var)

        if result==0:
            var = Database.upgradePassword(name, newPassword, oldPassword)

        if var ==1:
            messagebox.showinfo("Success","Upgraded Successfully")
            window.destroy()
            Homepage.homepage1(name)
        else:
            messagebox.showerror("Error","Failed")


    else:
        messagebox.showerror("Error", "password don't match")
def callme(name):
    import WindowInitializing
    root = WindowInitializing.window()
    start(root,name)
