from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
import os
from mutagen.mp3 import MP3
import time
import threading
import mysql.connector
import mysql
import DataBaseConnect
from tkinter.messagebox import *
import random
global textMusicCurrent
global textMusicLength
playlist = []
global playlistBox
global statusBar
global btnMute
global imageVolume
global scaleVolume
global imageMute
global path
global music_selected
global myresult






def select_music(root):
    global music_selected
    global path
    music_selected = playlistBox.curselection()
    music_selected = int(music_selected[0])
    music_play_path = playlist[music_selected]

    mydb, mycursor = DataBaseConnect.database()
    sql = ("""SELECT SongUrl FROM song WHERE SongName='%s' """ % (music_play_path))
    mycursor.execute(sql)
    url = mycursor.fetchall()
    path2 = url[0][0] + ".mp3"

    mixer.music.load(path2)
    time.sleep(1)
    mixer.music.play()
    statusBar['text'] = "Playing - " + os.path.basename(url[0][0])
    show_details(path2)

def user_ratingChange():
    print(index)
    print("new rating in user",value1)
    sys.path.append(r"C:\Users\M.Saood Sarwar\PycharmProjects\fyp\EBMPgui")

    from Signin import Geek

    p=Geek()
    val = p.getVal()
    print(val)
    mydb,mycursor = DataBaseConnect.database()

    sql = "INSERT INTO History (UserID,SongId,Rating) VALUES (%s, %s,%s)"
    val = (val, index, value1)
    mycursor.execute(sql, val)
    mydb.commit()
    var = mycursor.rowcount
    if var==1:
        print("Succss")


global index
def ratingChange():
    global myresult
    global index


    try:
        print(type(value1))
        val=float(value1)
        print("new rating in song", val)
        index=myresult[music_selected][1]
        mydb,mycursor=DataBaseConnect.database()


        sql = ("""SELECT NoOfRating FROM Song WHERE SongId='%s' """ % (index))
        mycursor.execute(sql)
        no_rating = mycursor.fetchall()

        sql = ("""SELECT TotalRating FROM Song WHERE SongId='%s' """ % (index))
        mycursor.execute(sql)
        total_rating = mycursor.fetchall()

        total_rating=total_rating[0][0]
        no_rating = no_rating[0][0]
        rating_update=((total_rating*no_rating)+val)/(no_rating+1)
        rating_update=round(rating_update,2)

        print(rating_update)
        mycursor.execute("""UPDATE Song SET TotalRating='%s' WHERE SongId=%s""",(rating_update, index))
        mydb.commit()
        updated = mycursor.rowcount

        new_no_rating=no_rating+1
        mycursor.execute("""UPDATE Song SET NoOfRating='%s' WHERE SongId=%s""", (new_no_rating, index))
        mydb.commit()
        updated1 = mycursor.rowcount
        if(updated==1 and updated1==1):
            showinfo("EBMP","Thanks")

    except:
        showerror("EBMP", "Error")
def two():
    ratingChange()
    user_ratingChange()

global value1
def report_change(name,value):
    global value1
    value1=value


def fill(myresult2,playlistBox,playlist):

    k = 0

    length = len(myresult2)
    while k<length:
        playlistBox.insert(k, myresult2[k][1])
        playlist.insert(k, myresult2[k][1])
        k=k+1
    return playlistBox,playlist

global var
def main(mood):
    import MusicSelection

    myresult=MusicSelection.database(mood)
    print(myresult)
    mydb, mycursor = DataBaseConnect.database()

    count=0
    myresult2=[]
    for i in myresult:
        sql = ("""SELECT SongUrl,SongName FROM Song WHERE SongId='%s' """ % (myresult[count][0]))
        mycursor.execute(sql)
        myresult1 = mycursor.fetchall()
        count=count+1
        myresult2.append(myresult1[0])

    print(myresult1)
    print(myresult2)
    root = Tk()
    root.geometry("1000x700")
    root.title("EBMP")
    root.iconbitmap(r'images/melody.ico')
    global var
    var = DoubleVar()
    scale = Scale(root,command=lambda value, name=var: report_change(name, value),variable=var, orient=HORIZONTAL, sliderlength=40, width=20, length=200, from_=0, to=10)
    scale.pack(anchor=CENTER)
    button = Button(root, text="Rate Song",command=two)
    button.pack(anchor=CENTER)
    label = Label(root)
    label.pack()


    menuBar = Menu(root)
    root.config(menu=menuBar)

    global statusBar
    statusBar = Label(root, text="Welcome to EBMP", relief=SUNKEN, anchor=W)
    statusBar.pack(side=BOTTOM, fill=X)

    subMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="File", menu=subMenu)

    subMenu.add_command(label="Exit", command=root.destroy)

    subMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label="About", command=submenu_about)

    mixer.init()

    frameLeft = Frame(root)
    frameLeft.pack(side=LEFT, padx=10,pady=80)
    global playlistBox
    playlistBox = Listbox(frameLeft, relief=RAISED,width=60)
    playlistBox.pack()
    button = Button(frameLeft, text="Refresh")
    button.pack(anchor=CENTER)

    #k=0
    #length = len(myresult)


    fill(myresult2,playlistBox,playlist)

    frameRight = Frame(root)
    frameRight.pack()

    frameTop = Frame(frameRight)
    frameTop.pack()

    textWelcome = Label(frameTop, text="Welcome to EBMP")
    textWelcome.pack(pady=5)

    global textMusicLength
    textMusicLength = Label(frameTop, text="Total Length: --:--")
    textMusicLength.pack()

    global textMusicCurrent
    textMusicCurrent = Label(frameTop, text="Current Time: --:--", relief=GROOVE)
    textMusicCurrent.pack(pady=5)

    frameMiddle = Frame(frameRight)
    frameMiddle.pack(padx=30, pady=30)

    imagePlay = PhotoImage(file=r'images/play.png')
    btnPlay = Button(frameMiddle, text="Play", command=lambda: music_play(myresult))
    btnPlay.grid(row=0, column=0, padx=10)

    imageStop = PhotoImage(file=r'images/stop.png')
    btnStop = Button(frameMiddle, text="Stop", command=music_stop)
    btnStop.grid(row=0, column=1, padx=10)

    imagePause = PhotoImage(file=r'images/pause.png')
    btnPause = Button(frameMiddle, text="Pause", command=music_pause)
    btnPause.grid(row=0, column=2, padx=10)

    frameBottom = Frame(frameRight)
    frameBottom.pack()

    imageRewind = PhotoImage(file=r'images/rewind.png')
    btnRewind = Button(frameBottom, text="Rewind", command=music_play)
    btnRewind.grid(row=0, column=0)

    select_button = Button(frameBottom, text="Select", command=lambda: select_music(root))
    select_button.grid(row=5, column=1)

    global btnMute
    imageMute = PhotoImage(file=r'images/mute.png')
    imageVolume = PhotoImage(file=r'images/volume.png')
    btnMute = Button(frameBottom, text="Volume", command=music_mute)
    btnMute.grid(row=0, column=1)

    scaleVolume = Scale(frameBottom, from_=0, to=100, orient=HORIZONTAL, command=music_volume)
    scaleVolume.set(80)
    scaleVolume.grid(row=0, column=2, padx=30, pady=15)



    root.protocol("WM_DELETE_WINDOW",lambda: on_exit(root))
    root.mainloop()





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







def submenu_about():
    tkinter.messagebox.showinfo("About", "Developed by Saood Sarwar")




# def onselect(evt):
#     # Note here that Tkinter passes an event object to onselect()
#     w = evt.widget
#     music_selected = w.curselection()
#     music_selected = int(music_selected[0])
#     music_play_path = playlist[music_selected]
#     mixer.music.load(music_play_path)





def music_play(myresult):
    global paused

    if paused:
        mixer.music.unpause()
        statusBar['text'] = "Playing - " + os.path.basename(textFilePath)
        paused = FALSE
    else:
        try:
            #music_stop()
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
    global btnMute

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





def on_exit(root):
    music_stop()
    root.destroy()

def call(mood):
    main(mood)
