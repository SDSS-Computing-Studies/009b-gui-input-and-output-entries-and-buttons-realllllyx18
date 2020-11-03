"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import * 
import math

window = tk.Tk()

eoutput = StringVar()
eoutput.set("Output part")

def clickFunction():
    num1 = e1.get()
    b = float(num1)
    num2 = e1.get()
    c = float(num2)
    answer = (-b+math.sqrt(b*2-4*c))/2 and (-b-math.sqrt(b*2-4*c))/2
    a_entry.delete(0,END)
    a_entry.insert(0,answer)

l1 = Label(window, text = "Enter the value of b")
e1 = Entry(window, width = 20)
l2 = Label(window, text = "Enter the value of c")
e2 = Entry(window, width = 20)
b1 = Button(window, text = "Click to calculate", command = clickFunction)
a_label = Label(window, text = "Answer goes here: ")
a_entry = Entry(window, width = 20, textvariable = eoutput)

l1.grid(row=1,column=1)
e1.grid(row=1,column=1)
l2.grid(row=1,column=1)
e2.grid(row=1,column=1)
b1.grid(row=1,column=1)
a_label.grid(row=2,column=1)
a_entry.grid(row=3,column=2)

window.mainloop




