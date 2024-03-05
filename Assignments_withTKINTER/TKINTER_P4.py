Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> win = Tk()
>>> f = Frame(win)
>>> b1 = Button(f, text = "One")
>>> b2 = Button(f, text = "Two")
>>> b3 = Button(f, text = "Three")
>>> b1.pack(side=LEFT)
>>> b2.pack(side=LEFT)
>>> b3.pack(side=LEFT)
>>> l = Label(win, text="This label is over all buttons")
>>> l.pack()
>>> f.pack()
>>> b1.configure(text="Uno")
>>> def but1():
...     print("Button one was pushed")
... 
...     
>>> b1.configure(command=but1)
>>> Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
Button one was pushed
