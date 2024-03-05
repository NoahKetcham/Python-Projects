Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> win = TK()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    win = TK()
NameError: name 'TK' is not defined
>>> b1 = Button(win, text="One")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b1 = Button(win, text="One")
NameError: name 'Button' is not defined
>>> win = Tk()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    win = Tk()
NameError: name 'Tk' is not defined
>>> from tkinter import *
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="Two")
>>> b1.grid(row=0, column = 0)
>>> b2.grid(row=1, column = 1)
>>> 1 = Label(win, text="This is a label")
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> l = Label(win, text="This is a label")
>>> l.grid(row=1, column=0)
