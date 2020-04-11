from tkinter import*

from PyQt5.QtCore import left
from pygame import surface

import Signin
import Upgrade
import cv2
import matplotlib.pyplot as plt
import WindowInitializing
import pygame
import sys
pygame.init()
pygame.mixer.music.load("DusBahane.mp3")
val=0

def logout(win):
    win.destroy()
    Signin.call()


def play1():
    pygame.mixer.music.play()

def stop1():
    pygame.mixer.music.stop()


def music_forward(event=None):
    print(val)




def homepage1(name):
    root = WindowInitializing.window()
    title = Label(root, text=name, font=("times new roman", 40, "bold"), bg="black", fg="white", bd=10,
                  relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)

    upgrade_frame = Frame(root, bg="white")
    upgrade_frame.place(x=100, y=130)
    btn_upgradeProfile = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="Upgrade Profile", command=lambda :upgradedata(root,name), bg="black", fg="white").grid(row=0, column=0)
    btn_history = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="History",  bg="black", fg="white").grid(row=0, column=2)
    btn_logout = Button(upgrade_frame,width=15,height=2,font=("times new roman", 20, "bold"), text="Logout" ,command=lambda :logout(root),  bg="black", fg="white").grid(row=0, column=3)

    login_frame = Frame(root, bg="white")
    login_frame.place(x=1100, y=130)
    btn_camera = Button(login_frame, text="camera",width=200,height=70, command=camera, image=root.camera, compound=LEFT,
                       font=("times new roman", 20, "bold"), bg="black", fg="white").grid(row=0, column=0)
    btn_musicPlay = Button(login_frame, text="music play", width=200, height=70, command=play1, image=root.camera, compound=LEFT,
                        font=("times new roman", 20, "bold"), bg="black", fg="white").grid(row=1, column=0)
    btn_musicStop = Button(login_frame, text="music stop", width=200, height=70, command=stop1, image=root.camera,
                       compound=LEFT,
                       font=("times new roman", 20, "bold"), bg="black", fg="white").grid(row=2, column=0)

    music_frame = Frame(root, bg="white")
    music_frame.place(x=100, y=500)
    music_scale = Scale(root, from_=0, to=400, orient=HORIZONTAL, length=300)
    music_scale.bind("<ButtonRelease-1>",music_forward)
    music_scale.place(x=0,y=0)
    val1 = music_scale.get()
    print(val1)


    root.mainloop()

def upgradedata(win,name):
    win.destroy()
    Upgrade.callme(name)

def camera():
    with add_path(r'C:\Users\M.Saood Sarwar\PycharmProjects\fyp\actual'):
        mod = __import__('mainstart')
    del sys.modules['mainstart']



class add_path():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass
