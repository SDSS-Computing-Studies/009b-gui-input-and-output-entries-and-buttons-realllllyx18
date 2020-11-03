"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import * 

window = tk.Tk()

eoutput = StringVar()
eoutput.set("Output part")

def clickFunction():
    word = e1.get()
    word2 = e2.get()
    word3 = e3.get()
    a_entry.delete(0,END)
    a_entry.insert(0,"Dear " + word + ", You are " + word2 + " invited!" + " It's time for a " + word3 + ".")

l1 = Label(window, text="Dear ")
e1 = Entry(window)
l2 = Label(window, text=",")
l3 = Label(window, text=" You are ")
e2 = Entry(window)
l4 = Label(window, text=" invited!\nIt's time for a ")
e3 = Entry(window)
l5 = Label(window, text="! ")
b1 = Button(window, text="Click to see output", command=clickFunction)
a_entry = Entry(window, width=70, textvariable=eoutput)

l1.pack()
e1.pack()
l2.pack()
l3.pack()
e2.pack()
l4.pack()
e3.pack()
l5.pack()
b1.pack()
a_entry.pack()

window.mainloop()


