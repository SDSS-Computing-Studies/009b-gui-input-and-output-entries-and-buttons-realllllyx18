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
#!python3

import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Factoring trinomials")

l1 = tk.Label(win, text="1.Enter the coefficients\n2.Press the Factor button to get the result")

l2 = tk.Label(win, text="x^2 +")
l3 = tk.Label(win, text="x +")
e1 = tk.Entry(win, width=1)
e2 = tk.Entry(win, width=1)
l4 = tk.Label(win, text=" = 0")

output = StringVar()
str1 = "Output goes here"
output.set(str1)
e3 = tk.Entry(win, width=len(str1), textvariable=output)

def factor():
    b = e1.get()
    c = e2.get()
    b = int(b)
    c = int(c)
    if b > 0:
        for i in range(1,c+1):
            if i + c/i == b:
                m = i
                n = int(c/i)
        output.set("(x + " + str(m) + ")(x +" + str(n) + ") = 0")
        
    if b < 0:
        for i in range(1,c+1):
            if i + c/i == -b:
                m = i
                n = int(c/i)
        output.set("(x - " + str(m) + ")(x -" + str(n) + ") = 0")

b1 = tk.Button(win, text="Factor", command=factor)

l1.grid(row=1, columnspan=6)
l2.grid(row=2, column=1)
e1.grid(row=2, column=2)
l3.grid(row=2, column=3)
e2.grid(row=2, column=4)
l4.grid(row=2, column=5)
b1.grid(row=3, column=3)
e3.grid(row=4, columnspan=8)


win.mainloop()




