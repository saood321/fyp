from tkinter import*
from PIL import ImageTk

def window():
    root = Tk()
    root.title("EBMP")
    root.geometry("1350x700+0+0")
    root.bg_icon = ImageTk.PhotoImage(file="img1.jpg")
    root.user_icon = ImageTk.PhotoImage(file="img2.png")
    root.password_icon = ImageTk.PhotoImage(file="img3.png")
    root.login_icon = ImageTk.PhotoImage(file="login.png")
    root.email_icon = ImageTk.PhotoImage(file="email.jpg")
    root.camera = ImageTk.PhotoImage(file="camera.png")
    bg_lbl =Label(root,image=root.bg_icon).pack()

    return root