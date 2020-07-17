from tkinter import *
win=Tk()
win.title('PokerChamp')
win.geometry('400x200')

background_image = PhotoImage(file=r'C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images/music.png')
background_label = Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root=Toplevel()

#root.config(bg='#1b800b')
root.title('PokerChamp')

image = PhotoImage(file=r'C:\Users\M.Saood Sarwar\PycharmProjects\fyp\images/main3.png')
label = Label(root, image=image)
label.place(relx=0, rely=0)