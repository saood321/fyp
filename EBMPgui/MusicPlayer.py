from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
import os
from mutagen.mp3 import MP3
import time
import threading

root = Tk()

root.title("EBMP")
#root.iconbitmap(r'images/melody.ico')

menuBar = Menu(root)
root.config(menu=menuBar)

statusBar = Label(root, text="Welcome to EBMP", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

playlist = []

def check(str):
    print(str)



def start_counter(length):
    global paused
    count = 0

    while count <= length and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(count, 60)
            mins = round(mins)
            secs = round(secs)

            formatCounter = '{:02d}:{:02d}'.format(mins, secs)
            textMusicCurrent['text'] = "Current Time - " + formatCounter

            time.sleep(1)
            count += 1


def show_details(filepath):
    splitFileName = os.path.splitext(filepath)

    if splitFileName[1] == '.mp3':
        totalLength = MP3(filepath).info.length
    elif splitFileName[1] == '.MP3':
        totalLength = MP3(filepath).info.length
    else:
        totalLength = mixer.Sound(filepath).get_length()

    mins, secs = divmod(totalLength, 60)
    mins = round(mins)
    secs = round(secs)

    formatLength = '{:02d}:{:02d}'.format(mins, secs)
    textMusicLength['text'] = "Total Length - " + formatLength

    threadCounter = threading.Thread(target=start_counter, args=(totalLength,))
    threadCounter.start()


def add_to_list_box(filename):
    filename = os.path.basename(filename)
    listIndex = 0

    playlistBox.insert(listIndex, filename)
    playlist.insert(listIndex, textFilePath)
    listIndex += 1


def browse_file():
    global textFilePath
    textFilePath = filedialog.askopenfilename()
    add_to_list_box(textFilePath)


subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def submenu_about():
    tkinter.messagebox.showinfo("About", "Developed by Abubakar Sheikh")


subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About", command=submenu_about)

mixer.init()

frameLeft = Frame(root)
frameLeft.pack(side=LEFT, padx=30)


# def onselect(evt):
#     # Note here that Tkinter passes an event object to onselect()
#     w = evt.widget
#     music_selected = w.curselection()
#     music_selected = int(music_selected[0])
#     music_play_path = playlist[music_selected]
#     mixer.music.load(music_play_path)


playlistBox = Listbox(frameLeft, relief=RAISED)
# playlistBox.bind('<<ListboxSelect>>', onselect)
playlistBox.pack()

btnAdd = Button(frameLeft, text="+ Add", command=browse_file)
btnAdd.pack(side=LEFT)

btnDel = Button(frameLeft, text="- Del")
btnDel.pack(side=LEFT)

frameRight = Frame(root)
frameRight.pack()

frameTop = Frame(frameRight)
frameTop.pack()

textWelcome = Label(frameTop, text="Welcome to EBMP")
textWelcome.pack(pady=5)

textMusicLength = Label(frameTop, text="Total Length: --:--")
textMusicLength.pack()

textMusicCurrent = Label(frameTop, text="Current Time: --:--", relief=GROOVE)
textMusicCurrent.pack(pady=5)


def music_play():
    global paused

    if paused:
        mixer.music.unpause()
        statusBar['text'] = "Playing - " + os.path.basename(textFilePath)
        paused = FALSE
    else:
        try:
            music_stop()

            music_selected = playlistBox.curselection()
            music_selected = int(music_selected[0])
            music_play_path = playlist[music_selected]
            mixer.music.load(music_play_path)
            time.sleep(1)
            mixer.music.play()
            statusBar['text'] = "Playing - " + os.path.basename(music_play_path)

            show_details(music_play_path)
        except:
            tkinter.messagebox.showerror("File not found", "Please open a file first")


def music_stop():
    global paused
    mixer.music.stop()
    statusBar['text'] = "Stopped"
    paused = FALSE


paused = FALSE


def music_pause():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusBar['text'] = "Paused"


muted = FALSE


def music_mute():
    global muted

    if muted:
        mixer.music.set_volume(0.8)
        btnMute.configure(image=imageVolume)
        scaleVolume.set(80)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        btnMute.configure(image=imageMute)
        scaleVolume.set(0)
        muted = TRUE


def music_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


frameMiddle = Frame(frameRight)
frameMiddle.pack(padx=30, pady=30)

imagePlay = PhotoImage(file=r'images/play.png')
btnPlay = Button(frameMiddle, image=imagePlay, command=music_play)
btnPlay.grid(row=0, column=0, padx=10)

imageStop = PhotoImage(file=r'images/stop.png')
btnStop = Button(frameMiddle, image=imageStop, command=music_stop)
btnStop.grid(row=0, column=1, padx=10)

imagePause = PhotoImage(file=r'images/pause.png')
btnPause = Button(frameMiddle, image=imagePause, command=music_pause)
btnPause.grid(row=0, column=2, padx=10)

frameBottom = Frame(frameRight)
frameBottom.pack()

imageRewind = PhotoImage(file=r'images/rewind.png')
btnRewind = Button(frameBottom, image=imageRewind, command=music_play)
btnRewind.grid(row=0, column=0)

imageMute = PhotoImage(file=r'images/mute.png')
imageVolume = PhotoImage(file=r'images/volume.png')
btnMute = Button(frameBottom, image=imageVolume, command=music_mute)
btnMute.grid(row=0, column=1)

scaleVolume = Scale(frameBottom, from_=0, to=100, orient=HORIZONTAL, command=music_volume)
scaleVolume.set(80)
scaleVolume.grid(row=0, column=2, padx=30, pady=15)


def on_exit():
    music_stop()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
