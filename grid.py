from tkinter import *

root = Tk()

# creating a label widget
myLabel1 = Label(root, text="Hello there!")
myLabel2 = Label(root, text="General Kenobi...")

# shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()

