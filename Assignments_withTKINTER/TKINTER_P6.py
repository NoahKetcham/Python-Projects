Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import from tkiner *
SyntaxError: invalid syntax
>>> from tkinter import *
>>> win = Tk()
>>> lb Listbox(win, height=3)
SyntaxError: invalid syntax
>>> lb = Listbox(win, height=3)
>>> lb.pack()
>>> lb.insert(END, "first entry")
>>> lb.insert(END, "second entry")
>>> lb.insert(END, "third entry")
>>> lb.insert(END, "fourth entry")
>>> 
>>> sb = Scrollbar(win, orient=VERTICAL)
>>> sb.pack(side=LEFT, fill+Y)
SyntaxError: positional argument follows keyword argument
>>> sb.pack(side=LEFT, fill=Y)
>>> 
>>> sb.configure(command=lb.yview)
>>> lb.configure(yscrollcommand=sb.set)
>>> 
>>> lb.curselection()
(2,)
>>> lb.curselection()
(1,)
