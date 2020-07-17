from tkinter import *
master = Tk()
def ok(value):
    print (value)
options = ["1", "2", "3"]
var = StringVar()

drop = OptionMenu(master, var, *options, command=ok)
drop.place(x=10, y=10)
 #etc

mainloop()
